PYTHON ?= python
NAME := $(shell "$(PYTHON)" setup.py --name)
VERSION := $(shell "$(PYTHON)" setup.py --version)
RPMBUILD_OPTIONS :=

all: install

install test egg_info:
	"$(PYTHON)" setup.py $@

clean:
	rm -rf dist/ build/ cover/

sdist bdist_wheel: egg_info clean
	"$(PYTHON)" setup.py $@

dist: sdist bdist_wheel

deb: sdist
	rename 's/-([0-9.]+)\.tar\.gz$$/_$$1.orig.tar.gz/' dist/$(NAME)-$(VERSION).tar.gz
	cd dist && tar xavf $(NAME)_$(VERSION).orig.tar.gz
	cp -arf pkg/debian dist/$(NAME)-$(VERSION)/
	sed -i -e 's/#pkg_version#/$(VERSION)/' dist/$(NAME)-$(VERSION)/debian/changelog
	cd dist/$(NAME)-$(VERSION)/ && dpkg-buildpackage

rpm: sdist
	rpmbuild -ba pkg/python-$(NAME).spec                   \
	    --define 'pkg_version $(VERSION)'                  \
	    --define 'curdir $(CURDIR)'                        \
	    --define '_topdir $(CURDIR)/dist'                  \
	    --define '_sourcedir $(CURDIR)/dist'               \
	    --define '_builddir $(CURDIR)/build/BUILD'         \
	    --define '_buildrootdir $(CURDIR)/build/BUILDROOT' \
	    $(RPMBUILD_OPTIONS)

upload: dist
	twine upload $(wildcard dist/*.tar.gz dist/*.whl)

.PHONY: all install dist egg_info sdist bdist_wheel test deb rpm upload clean

# ex:set ts=4 noet:
