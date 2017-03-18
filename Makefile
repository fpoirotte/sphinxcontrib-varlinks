NAME := sphinxcontrib-varlinks
VERSION := 0.0.0

all: install

install sdist bdist_wheel test:
	python setup.py $@

egg_info:
	python setup.py $@
	$(eval VERSION=$(shell grep ^Version: sphinxcontrib_varlinks.egg-info/PKG-INFO | awk '{print $$2}'))

dist: sdist bdist_wheel

deb: sdist egg_info
	rename 's/-([0-9.]+)\.tar\.gz$$/_$$1.orig.tar.gz/' dist/$(NAME)-$(VERSION).tar.gz
	cd dist && tar xavf $(NAME)_$(VERSION).orig.tar.gz
	cp -arf pkg/debian dist/$(NAME)-$(VERSION)/
	cd dist/$(NAME)-$(VERSION)/ && dpkg-buildpackage

rpm: sdist
	rpmbuild -ba pkg/python-$(NAME).spec      \
	    --define '_topdir ./dist'             \
	    --define '_sourcedir ./dist'          \
	    --define '_builddir ./build/BUILD'    \
	    --define '_buildrootdir ./build/BUILDROOT'

.PHONY: all install dist sdist bdist_wheel test deb rpm

# ex:set ts=4 noet:
