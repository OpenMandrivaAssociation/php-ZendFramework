%undefine __find_provides
%undefine __find_requires

%define php_name ZendFramework

Summary:	Leading open-source PHP framework
Name:		php-ZendFramework
Version:	1.11.11
Release:	2
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
Requires:	php-pdo
Requires:	php-posix
Requires:	php-session
Requires:	php-simplexml
Requires:	php-xml
Requires:	php-zlib
BuildArch:	noarch

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
Requires:	php-pear-PHPUnit >= 3.0.0
Requires:	php-channel-phpunit
Requires:	fonts-ttf-bitstream-vera
BuildRequires:	fonts-ttf-bitstream-vera

%description	tests
This package includes Zend Framework unit tests for all available subpackages.

%package	extras
Summary:	Zend Framework Extras (ZendX)
Group:		Development/PHP
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-ZendX = %{version}-%{release}

%description	extras
This package includes the ZendX libraries.

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

#package	Cache-Backend-Sqlite
#Summary:	Zend Framework sqlite back end
#Group:		Development/PHP
#Requires:	%{name} = %{version}-%{release}
#Requires:	php-sqlite

#description Cache-Backend-Sqlite
#This package contains the back end for Zend_Cache to store and retrieve data
#via sqlite databases.

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

#package	Db-Adapter-Mysqli
#Summary:	Zend Framework database adapter for mysqli
#Group:		Development/PHP
#Requires:	%{name} = %{version}-%{release}
#Requires:	php-mysqli

#description	Db-Adapter-Mysqli
#This package contains the files for Zend Framework necessary to connect to a
#MySQL database via mysqli connector.

#package Db-Adapter-Db2
#Summary:  Zend Framework database adapter for DB2
#Group:    Development/PHP
#Requires: %{name} = %{version}-%{release}
#Requires: php-ibm_db2 # Not available in Mandriva's PHP

#description Db-Adapter-Db2
#This package contains the files for Zend Framework necessary to connect to an
#IBM DB2 database.

#package	Db-Adapter-Firebird
#Summary:	Zend Framework database adapter for InterBase
#Group:		Development/PHP
#Requires:	%{name} = %{version}-%{release}
#Requires:	php-interbase

#description Db-Adapter-Firebird
#This package contains the files for Zend Framework necessary to connect to a
#Firebird/InterBase database.

#package Db-Adapter-Oracle
#Summary:  Zend Framework database adapter for Oracle
#Group:    Development/PHP
#Requires: %{name} = %{version}-%{release}
#Requires: php-oci8 # Not available in Mandriva's PHP

#description Db-Adapter-Oracle
#This package contains the files for Zend Framework necessary to connect to an
#Oracle database.

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
Requires:	php-bitset

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

%{__cat} executables valid_executables|sort|uniq -u > invalid_executables


%install
%{__mkdir_p} %{buildroot}%{_datadir}/php
cp -r library/Zend %{buildroot}%{_datadir}/php
cp -r demos/Zend %{buildroot}%{_datadir}/php/Zend/demos
cp -r tests %{buildroot}%{_datadir}/php/Zend
cp -r externals %{buildroot}%{_datadir}/php/Zend

# ZendX
cd extras
cp -r library/ZendX %{buildroot}%{_datadir}/php
cp -r tests %{buildroot}%{_datadir}/php/ZendX
cd ..

# rhbz 477440
pushd %{buildroot}%{_datadir}/php/Zend/tests/Zend/Pdf/_fonts
    for i in *.ttf; do
	ln -snf %{_datadir}/fonts/TTF/$i $i
    done
popd

%files
%{_datadir}/php/Zend
%exclude %{_datadir}/php/Zend/demos
%exclude %{_datadir}/php/Zend/tests
%exclude %{_datadir}/php/Zend/Cache/Backend/Apc.php
%exclude %{_datadir}/php/Zend/Cache/Backend/Memcached.php
%exclude %{_datadir}/php/Zend/Captcha
%exclude %{_datadir}/php/Zend/Dojo.php
%exclude %{_datadir}/php/Zend/Dojo
%exclude %{_datadir}/php/Zend/Feed.php
%exclude %{_datadir}/php/Zend/Feed
%exclude %{_datadir}/php/Zend/Gdata.php
%exclude %{_datadir}/php/Zend/Gdata
%exclude %{_datadir}/php/Zend/Pdf.php
%exclude %{_datadir}/php/Zend/Pdf
%exclude %{_datadir}/php/Zend/Search
%exclude %{_datadir}/php/Zend/Service/Akismet.php
%exclude %{_datadir}/php/Zend/Service/Amazon.php
%exclude %{_datadir}/php/Zend/Service/Amazon
%exclude %{_datadir}/php/Zend/Service/Audioscrobbler.php
%exclude %{_datadir}/php/Zend/Service/Delicious.php
%exclude %{_datadir}/php/Zend/Service/Delicious
%exclude %{_datadir}/php/Zend/Service/Flickr.php
%exclude %{_datadir}/php/Zend/Service/Flickr
%exclude %{_datadir}/php/Zend/Service/Nirvanix.php
%exclude %{_datadir}/php/Zend/Service/Nirvanix
%exclude %{_datadir}/php/Zend/Service/ReCaptcha.php
%exclude %{_datadir}/php/Zend/Service/ReCaptcha
%exclude %{_datadir}/php/Zend/Service/Simpy.php
%exclude %{_datadir}/php/Zend/Service/Simpy
%exclude %{_datadir}/php/Zend/Service/SlideShare.php
%exclude %{_datadir}/php/Zend/Service/SlideShare
%exclude %{_datadir}/php/Zend/Service/StrikeIron.php
%exclude %{_datadir}/php/Zend/Service/StrikeIron
%exclude %{_datadir}/php/Zend/Service/Technorati.php
%exclude %{_datadir}/php/Zend/Service/Technorati
%exclude %{_datadir}/php/Zend/Service/Yahoo.php
%exclude %{_datadir}/php/Zend/Service/Yahoo
%exclude %{_datadir}/php/Zend/externals/dojo

%doc LICENSE.txt INSTALL.txt README.txt

%files demos
%{_datadir}/php/Zend/demos
%doc LICENSE.txt

%files tests
%{_datadir}/php/Zend/tests
%doc LICENSE.txt

%files extras
%{_datadir}/php/ZendX
%doc LICENSE.txt

%files Cache-Backend-Apc
%{_datadir}/php/Zend/Cache/Backend/Apc.php
%doc LICENSE.txt

%files Cache-Backend-Memcached
%{_datadir}/php/Zend/Cache/Backend/Memcached.php
%doc LICENSE.txt

%files Captcha
%{_datadir}/php/Zend/Captcha
%doc LICENSE.txt

%files Dojo
%{_datadir}/php/Zend/Dojo.php
%{_datadir}/php/Zend/Dojo
%{_datadir}/php/Zend/externals/dojo
%doc LICENSE.txt

%files Feed
%{_datadir}/php/Zend/Feed.php
%{_datadir}/php/Zend/Feed
%doc LICENSE.txt

%files Gdata
%{_datadir}/php/Zend/Gdata.php
%{_datadir}/php/Zend/Gdata
%doc LICENSE.txt

%files Pdf
%{_datadir}/php/Zend/Pdf.php
%{_datadir}/php/Zend/Pdf
%doc LICENSE.txt

%files Search-Lucene
%{_datadir}/php/Zend/Search
%doc LICENSE.txt

%files Services
%{_datadir}/php/Zend/Service/Akismet.php
%{_datadir}/php/Zend/Service/Amazon.php
%{_datadir}/php/Zend/Service/Amazon
%{_datadir}/php/Zend/Service/Audioscrobbler.php
%{_datadir}/php/Zend/Service/Delicious.php
%{_datadir}/php/Zend/Service/Delicious
%{_datadir}/php/Zend/Service/Flickr.php
%{_datadir}/php/Zend/Service/Flickr
%{_datadir}/php/Zend/Service/Nirvanix.php
%{_datadir}/php/Zend/Service/Nirvanix
%{_datadir}/php/Zend/Service/ReCaptcha.php
%{_datadir}/php/Zend/Service/ReCaptcha
%{_datadir}/php/Zend/Service/Simpy.php
%{_datadir}/php/Zend/Service/Simpy
%{_datadir}/php/Zend/Service/SlideShare.php
%{_datadir}/php/Zend/Service/SlideShare
%{_datadir}/php/Zend/Service/StrikeIron.php
%{_datadir}/php/Zend/Service/StrikeIron
%{_datadir}/php/Zend/Service/Technorati.php
%{_datadir}/php/Zend/Service/Technorati
%{_datadir}/php/Zend/Service/Yahoo.php
%{_datadir}/php/Zend/Service/Yahoo
%doc LICENSE.txt


%changelog
* Sun Dec 18 2011 Oden Eriksson <oeriksson@mandriva.com> 1.11.11-1mdv2012.0
+ Revision: 743481
- 1.11.11

* Fri Aug 12 2011 Oden Eriksson <oeriksson@mandriva.com> 1.11.10-1
+ Revision: 694093
- 1.11.10

* Sun Jun 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1.11.7-1
+ Revision: 685972
- 1.11.7

* Mon Mar 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.11.4-1
+ Revision: 642441
- 1.11.4

* Thu Feb 17 2011 Oden Eriksson <oeriksson@mandriva.com> 1.11.3-1
+ Revision: 638134
- 1.11.3

* Sat Jan 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.11.0-1mdv2011.0
+ Revision: 627263
- new version

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.7.5-2mdv2010.0
+ Revision: 441781
- rebuild

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1.7.5-1mdv2009.1
+ Revision: 341700
- 1.7.5
- sync slightly with fedora, but fix the symlink mess (duh!)

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-2mdv2009.1
+ Revision: 321697
- rebuild

* Tue Oct 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-1mdv2009.1
+ Revision: 297910
- import php-ZendFramework


* Tue Oct 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.0-1mdv2009.0
- initial Mandriva package (fedora import and adaptation)
