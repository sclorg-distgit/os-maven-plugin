%{?scl:%scl_package os-maven-plugin}
%{!?scl:%global pkg_name %{name}}

%global vertag Final

Name:           %{?scl_prefix}os-maven-plugin
Version:        1.2.3
Release:        7.1%{?dist}
Summary:        Maven plugin for generating platform-dependent properties
License:        ASL 2.0
URL:            https://github.com/trustin/os-maven-plugin/
BuildArch:      noarch

Source0:        https://github.com/trustin/%{pkg_name}/archive/%{pkg_name}-%{version}.Final.tar.gz

Patch0:         0001-Port-to-current-plexus-utils.patch
Patch1:         0002-Don-t-fail-on-unknown-arch.patch

BuildRequires:  %{?scl_prefix_maven}maven-local
BuildRequires:  %{?scl_prefix_maven}mvn(junit:junit)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  %{?scl_prefix_maven}mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  %{?scl_prefix_maven}mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  %{?scl_prefix_maven}mvn(org.sonatype.oss:oss-parent:pom:)

%description
os-maven-plugin is a Maven extension/plugin that generates various
useful platform-dependent project properties normalized from
${os.name} and ${os.arch}.

${os.name} and ${os.arch} are often subtly different between JVM and
operating system versions or they sometimes contain machine-unfriendly
characters such as whitespaces. This plugin tries to remove such
fragmentation so that you can determine the current operating system
and architecture reliably.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}.%{vertag}

%patch0 -p1
%patch1 -p1

# Remove Eclipse plugin (not needed in Fedora)
%pom_remove_dep org.eclipse:ui
%pom_remove_plugin :maven-jar-plugin
find -name EclipseStartup.java -delete
find -name plugin.xml -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Jun 23 2017 Michael Simacek <msimacek@redhat.com> - 1.2.3-7.1
- Package import and sclization

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.3-6
- Regenerate build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.3-4
- Don't fail on unknown arch

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Michael Simacek <msimacek@redhat.com> - 1.2.3-2
- Port to current plexus-utils

* Tue Jul  8 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.3-1
- Initial pagkaging
