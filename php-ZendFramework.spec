%undefine __find_provides
%undefine __find_requires

%define php_name ZendFramework

Summary:	Leading open-source PHP framework
Name:		php-ZendFramework
Version:	1.6.0
Release:	%mkrel 1
License:	BSD
Group:		Development/PHP
URL:		http://framework.zend.com/
Source0:	http://framework.zend.com/releases/%{php_name}-%{version}/%{php_name}-%{version}.tar.gz
Requires:	php >= 5.1.4
Requires:	php-bcmath
Requires:	php-ctype
Requires:	php-curl
Requires:	php-dom
Requires:	php-fileinfo
Requires:	php-hash
Requires:	php-iconv
Requires:	php-json
Requires:	php-pcre
Requires:	php-posix
Requires:	php-session
Requires:	php-simplexml
Requires:	php-zlib
BuildRequires:	symlinks
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Extending the art & spirit of PHP, Zend Framework is based on simplicity,
object-oriented best practices, corporate friendly licensing, and a rigorously
tested agile codebase. Zend Framework is focused on building more secure,
reliable, and modern Web 2.0 applications & web services, and consuming widely
available APIs from leading vendors like Google, Amazon, Yahoo!, Flickr, as
well as API providers and catalogers like StrikeIron and ProgrammableWeb.

%package	demos
Summary:	Demos for the Zend Framework
Group:		Development/PHP
Requires:	%{name} = %{version}-%{release}

%description	demos
This package includes Zend Framework demos for the Feeds, Gdata, Mail, OpenId,
Pdf, Search-Lucene and Services subpackages.

%package	tests
Summary:	Unit tests for the Zend Framework
Group:		Development/PHP
Requires:	%{name} = %{version}-%{release}
#Requires:	php-pear(pear.phpunit.de/PHPUnit) >= 3.0.0

%description	tests
This package includes Zend Framework unit tests for all available subpackages.

%package	Cache-Backend-Apc
Summary:	Zend Framework APC cache backend
Group:		Development/PHP
Requires:	%{name} = %{version}-%{release}
Requires:	php-apc

%description	Cache-Backend-Apc
This package contains the backend for Zend_Cache to store and retrieve data via
APC.

%package	Cache-Backend-Memcached
Summary:	Zend Framework memcache cache backend
Group:		Development/PHP
Requires:	%{name} = %{version}-%{release}
Requires:	php-memcache

%description	Cache-Backend-Memcached
This package contains the back end for Zend_Cache to store and retrieve data
via memcache.

%package	Captcha
Summary:	Zend Framework CAPTCHA component
Group:		Development/PHP
Requires:	%{name} = %{version}-%{release}
Requires:	php-gd

%description	Captcha
This package contains the Zend Framework CAPTCHA extension.

%package	Dojo
Summary:	Zend Framework Dojo Toolkit integration component
Group:		Development/PHP
Requires:	%{name} = %{version}-%{release}

%description	Dojo
This package contains the Zend Framework Dojo Toolkit component as well as a
copy of Dojo itself.

%package	Feed
Summary:	Live syndication feeds helper
Group:		Development/PHP
Requires:	%{name} = %{version}-%{release}
Requires:	php-mbstring

%description	Feed
This component provides a very simple way to work with live syndicated feeds.

* consumes RSS and Atom feeds
* provides utilities for discovering feed links
* imports feeds from multiple sources
* providers feed building and posting operations

%package	Gdata
Summary:	Google Data APIs
Group:		Development/PHP
Requires:	%{name} = %{version}-%{release}

%description	Gdata
The Google Data APIs provide read/write access to such services hosted at
google.com as Spreadsheets, Calendar, Blogger, and CodeSearch.

* supports both authentication mechanisms of Google Data servers
* supports queries and posting changes against Google Data services
* supports service-specific element types in an object-oriented interface
* matches functionality and design of other Google Data API clients

%package	Pdf
Summary:	PDF file handling helper
Group:		Development/PHP
Requires:	%{name} = %{version}-%{release}
Requires:	php-gd

%description	Pdf
Portable Document Format (PDF) from Adobe is the de facto standard for
cross-platform rich documents. Now, PHP applications can create or read PDF
documents on the fly, without the need to call utilities from the shell, depend
on PHP extensions, or pay licensing fees. Zend_Pdf can even modify existing PDF
documents.

* supports Adobe PDF file format
* parses PDF structure and provides access to elements
* creates or modifies PDF documents
* utilizes memory efficiently

%package	Search-Lucene
Summary:	Apache Lucene engine PHP port
Group:		Development/PHP
Requires:	%{name} = %{version}-%{release}
# php-pecl-bitset is not available but this is an optional requirement
# Requires: php-bitset

%description	Search-Lucene
The Apache Lucene engine is a powerful, feature-rich Java search engine that is
flexible about document storage and supports many complex query
types. Zend_Search_Lucene is a port of this engine written entirely in PHP 5.

* allows PHP-powered websites to leverage powerful search capabilities without
  the need for web services or Java
* provides binary compatibility with Apache Lucene
* matches Apache Lucene in performance

%package	Services
Summary:	Web service APIs for a number of providers
Group:		Development/PHP
Requires:	%{name} = %{version}-%{release}

%description	Services
This package contains web service client APIs for the following services:

- Akismet
- Amazon
- Audioscrobbler
- del.icio.us
- Flickr
- Nirvanix
- Simpy
- SlideShare
- StrikeIron
- Technorati
- Yahoo!

%prep

%setup -qn %{php_name}-%{version}

%build
find . -type f -perm /111 \
  -fprint executables -exec %{__chmod} -x '{}' \; >/dev/null

find . -type f -name \*.sh \
  -fprint valid_executables -exec %{__chmod} +x '{}' \; >/dev/null

cat executables valid_executables|sort|uniq -u > invalid_executables

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear
cp -pr library/Zend %{buildroot}%{_datadir}/pear
cp -pr demos/Zend %{buildroot}%{_datadir}/pear/Zend/demos
cp -pr tests %{buildroot}%{_datadir}/pear/Zend
cp -pr externals %{buildroot}%{_datadir}/pear/Zend
cp -pr laboratory/Zend_Tool/library/ZendL %{buildroot}%{_datadir}/pear
cp -pr laboratory/Zend_Tool/tests %{buildroot}%{_datadir}/pear/ZendL
cp -pr laboratory/Zend_Tool/bin/zf.{php,sh} %{buildroot}%{_datadir}/pear/ZendL

install -d %{buildroot}%{_bindir}
ln -s %{buildroot}%{_datadir}/pear/ZendL/zf.sh %{buildroot}%{_bindir}/zf
symlinks -c %{buildroot}%{_bindir} > /dev/null

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.txt INSTALL.txt README.txt
%{_datadir}/pear/Zend
%exclude %{_datadir}/pear/Zend/demos
%exclude %{_datadir}/pear/Zend/tests
%exclude %{_datadir}/pear/Zend/Cache/Backend/Apc.php
%exclude %{_datadir}/pear/Zend/Cache/Backend/Memcached.php
%exclude %{_datadir}/pear/Zend/Captcha
%exclude %{_datadir}/pear/Zend/Dojo.php
%exclude %{_datadir}/pear/Zend/Dojo
%exclude %{_datadir}/pear/Zend/Feed.php
%exclude %{_datadir}/pear/Zend/Feed
%exclude %{_datadir}/pear/Zend/Gdata.php
%exclude %{_datadir}/pear/Zend/Gdata
%exclude %{_datadir}/pear/Zend/Pdf.php
%exclude %{_datadir}/pear/Zend/Pdf
%exclude %{_datadir}/pear/Zend/Search
%exclude %{_datadir}/pear/Zend/Service/Akismet.php
%exclude %{_datadir}/pear/Zend/Service/Amazon.php
%exclude %{_datadir}/pear/Zend/Service/Amazon
%exclude %{_datadir}/pear/Zend/Service/Audioscrobbler.php
%exclude %{_datadir}/pear/Zend/Service/Delicious.php
%exclude %{_datadir}/pear/Zend/Service/Delicious
%exclude %{_datadir}/pear/Zend/Service/Flickr.php
%exclude %{_datadir}/pear/Zend/Service/Flickr
%exclude %{_datadir}/pear/Zend/Service/Nirvanix.php
%exclude %{_datadir}/pear/Zend/Service/Nirvanix
%exclude %{_datadir}/pear/Zend/Service/ReCaptcha.php
%exclude %{_datadir}/pear/Zend/Service/ReCaptcha
%exclude %{_datadir}/pear/Zend/Service/Simpy.php
%exclude %{_datadir}/pear/Zend/Service/Simpy
%exclude %{_datadir}/pear/Zend/Service/SlideShare.php
%exclude %{_datadir}/pear/Zend/Service/SlideShare
%exclude %{_datadir}/pear/Zend/Service/StrikeIron.php
%exclude %{_datadir}/pear/Zend/Service/StrikeIron
%exclude %{_datadir}/pear/Zend/Service/Technorati.php
%exclude %{_datadir}/pear/Zend/Service/Technorati
%exclude %{_datadir}/pear/Zend/Service/Yahoo.php
%exclude %{_datadir}/pear/Zend/Service/Yahoo
%exclude %{_datadir}/pear/Zend/externals/dojo
%{_datadir}/pear/ZendL
%{_bindir}/zf

%files demos
%defattr(-,root,root,-)
%{_datadir}/pear/Zend/demos

%files tests
%defattr(-,root,root,-)
%{_datadir}/pear/Zend/tests

%files Cache-Backend-Apc
%defattr(-,root,root,-)
%{_datadir}/pear/Zend/Cache/Backend/Apc.php

%files Cache-Backend-Memcached
%defattr(-,root,root,-)
%{_datadir}/pear/Zend/Cache/Backend/Memcached.php

%files Captcha
%defattr(-,root,root,-)
%{_datadir}/pear/Zend/Captcha

%files Dojo
%defattr(-,root,root,-)
%{_datadir}/pear/Zend/Dojo.php
%{_datadir}/pear/Zend/Dojo
%{_datadir}/pear/Zend/externals/dojo

%files Feed
%defattr(-,root,root,-)
%{_datadir}/pear/Zend/Feed.php
%{_datadir}/pear/Zend/Feed

%files Gdata
%defattr(-,root,root,-)
%{_datadir}/pear/Zend/Gdata.php
%{_datadir}/pear/Zend/Gdata

%files Pdf
%defattr(-,root,root,-)
%{_datadir}/pear/Zend/Pdf.php
%{_datadir}/pear/Zend/Pdf

%files Search-Lucene
%defattr(-,root,root,-)
%{_datadir}/pear/Zend/Search

%files Services
%defattr(-,root,root,-)
%{_datadir}/pear/Zend/Service/Akismet.php
%{_datadir}/pear/Zend/Service/Amazon.php
%{_datadir}/pear/Zend/Service/Amazon
%{_datadir}/pear/Zend/Service/Audioscrobbler.php
%{_datadir}/pear/Zend/Service/Delicious.php
%{_datadir}/pear/Zend/Service/Delicious
%{_datadir}/pear/Zend/Service/Flickr.php
%{_datadir}/pear/Zend/Service/Flickr
%{_datadir}/pear/Zend/Service/Nirvanix.php
%{_datadir}/pear/Zend/Service/Nirvanix
%{_datadir}/pear/Zend/Service/ReCaptcha.php
%{_datadir}/pear/Zend/Service/ReCaptcha
%{_datadir}/pear/Zend/Service/Simpy.php
%{_datadir}/pear/Zend/Service/Simpy
%{_datadir}/pear/Zend/Service/SlideShare.php
%{_datadir}/pear/Zend/Service/SlideShare
%{_datadir}/pear/Zend/Service/StrikeIron.php
%{_datadir}/pear/Zend/Service/StrikeIron
%{_datadir}/pear/Zend/Service/Technorati.php
%{_datadir}/pear/Zend/Service/Technorati
%{_datadir}/pear/Zend/Service/Yahoo.php
%{_datadir}/pear/Zend/Service/Yahoo

