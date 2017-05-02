Name     : golang-github-client9-gospell
Version  : 90dfc71015dfebd3a7274f1ad2756c1dbf09e250
Release  : 3
URL      : https://github.com/client9/gospell/archive/90dfc71015dfebd3a7274f1ad2756c1dbf09e250.tar.gz
Source0  : https://github.com/client9/gospell/archive/90dfc71015dfebd3a7274f1ad2756c1dbf09e250.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go
BuildRequires : golang-googlecode-go-net
BuildRequires : golang-github-naoina-toml
BuildRequires : golang-github-ryanuber-go-glob
BuildRequires : golang-github-naoina-go-stringutil
BuildRequires : golang-github-client9-plaintext 

%description
# gospell
[![Build Status](https://travis-ci.org/client9/gospell.svg?branch=master)](https://travis-ci.org/client9/gospell) [![Go Report Card](http://goreportcard.com/badge/client9/gospell)](http://goreportcard.com/report/client9/gospell) [![GoDoc](https://godoc.org/github.com/client9/gospell?status.svg)](https://godoc.org/github.com/client9/gospell) [![Coverage](http://gocover.io/_badge/github.com/client9/gospell)](http://gocover.io/github.com/client9/gospell) [![license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://raw.githubusercontent.com/client9/gospell/master/LICENSE)

%prep
%setup -q -n gospell-90dfc71015dfebd3a7274f1ad2756c1dbf09e250

%build
export LANG=C
mkdir -p build-dir/src/github.com/client9/
ln -s $(pwd) build-dir/src/github.com/client9/gospell
export GOPATH=$(pwd)/build-dir:/usr/lib/golang
pushd build-dir
    go build github.com/client9/gospell/cmd/gospell
popd

%install
rm -rf %{buildroot}
%global gopath /usr/lib/golang
%global library_path github.com/client9/gospell
mkdir -p %{buildroot}/usr/bin

install -p -m 755 build-dir/gospell %{buildroot}/usr/bin

# Copy all *.go and *.s files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in go s src golden template; do
    for file in $(find . -iname "*.$ext") ; do
        install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
        cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
    done
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}/... || :

%files
%defattr(-,root,root,-)
/usr/bin/gospell
/usr/lib/golang/src/github.com/client9/gospell/aff.go
/usr/lib/golang/src/github.com/client9/gospell/aff_test.go
/usr/lib/golang/src/github.com/client9/gospell/case.go
/usr/lib/golang/src/github.com/client9/gospell/case_test.go
/usr/lib/golang/src/github.com/client9/gospell/cmd/gospell/main.go
/usr/lib/golang/src/github.com/client9/gospell/cmd/sample/sample.go
/usr/lib/golang/src/github.com/client9/gospell/file.go
/usr/lib/golang/src/github.com/client9/gospell/gospell.go
/usr/lib/golang/src/github.com/client9/gospell/notwords.go
/usr/lib/golang/src/github.com/client9/gospell/notwords_test.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/cmd/plaintext/main.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/golang.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/html.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/html_test.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/identity.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/identity_test.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/markdown.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/markdown_test.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/mime.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/script.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/script_test.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/template.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/template_test.go
/usr/lib/golang/src/github.com/client9/gospell/plaintext/text.go
/usr/lib/golang/src/github.com/client9/gospell/words.go
/usr/lib/golang/src/github.com/client9/gospell/words_test.go
