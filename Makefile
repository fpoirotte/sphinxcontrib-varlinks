VERSION := 0.0.0

all: install

install sdist bdist_wheel:
	python setup.py $@

egg_info:
	python setup.py $@
	$(eval VERSION=$(shell grep ^Version: sphinxcontrib_varlinks.egg-info/PKG-INFO | awk '{print $$2}'))

dist: sdist bdist_wheel

deb: sdist egg_info
	rename 's/-([0-9.]+)\.tar\.gz$$/_$$1.orig.tar.gz/' dist/sphinxcontrib-varlinks-$(VERSION).tar.gz
	cd dist && tar xavf sphinxcontrib-varlinks_$(VERSION).orig.tar.gz
	cp -arf pkg/debian dist/sphinxcontrib-varlinks-$(VERSION)/
	cd dist/sphinxcontrib-varlinks-$(VERSION)/ && dpkg-buildpackage
