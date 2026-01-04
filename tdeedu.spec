%bcond clang 1
%bcond kig 1
%bcond v4l 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 3

%define tde_pkg tdeedu
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Summary:		Educational/Edutainment applications
Group:			System/GUI/Other
Version:		%{tde_version}
Release:		%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:		%{name}-rpmlintrc

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DXDG_MENU_INSTALL_DIR=%{_sysconfdir}/xdg/menus
BuildOption:    -DWITH_ALL_OPTIONS=ON -DWITH_OCAML_SOLVER=OFF
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:    -DBUILD_KIG=%{?!with_kig:OFF}%{?with_kig:ON}
BuildOption:    -DWITH_KIG_PYTHON_SCRIPTING=%{?!with_kig:OFF}%{?with_kig:ON}
BuildOption:    -DWITH_V4L=%{?!with_v4l:OFF}%{?with_v4l:ON}

BuildRequires: trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires: desktop-file-utils

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	fdupes
BuildRequires:	doxygen

# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# LIBUSB support
BuildRequires:  pkgconfig(libusb) pkgconfig(libusb-1.0)

# PYTHON3 support
%global python python
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
BuildRequires:	%{python}
BuildRequires:	%{python}-devel

# BOOST support
BuildRequires:	boost-devel
BuildRequires:  cmake(boost_python)

# OCAML support
BuildRequires: ocaml

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

Obsoletes:		trinity-kdeedu < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdeedu = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-kdeedu-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-kdeedu-libs = %{?epoch:%{epoch}:}%{version}-%{release}

# Meta-package
Requires: %{name}-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-blinken = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kalzium = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kalzium-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kanagram = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kbruch = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-keduca = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kgeography = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kgeography-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-khangman = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with kig}
Requires: trinity-kig = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires: trinity-kiten = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-klatin = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-klettres = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-klettres-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kmplot = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kpercentage = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kstars = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kstars-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ktouch = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kturtle = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kverbos = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kvoctrain = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kwordquiz = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-libtdeedu3 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-libkiten1 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-indi = %{?epoch:%{epoch}:}%{version}-%{release}


%description
Educational/Edutainment applications, including:
* blinken: Simon Says Game
* kalzium: Periodic Table of Elements
* kanagram: Letter Order Game
* kbruch: Exercise Fractions
* keduca: Tests and Exams
* kgeography: Geography Trainer
* khangman: Hangman Game
%if %{with kig}
* kig: Interactive Geometry
%endif
* kiten: Japanese Reference/Study Tool
* klatin: Latin Reviser
* klettres: French alphabet tutor
* kmplot: Mathematical Function Plotter
* kpercentage: Excersie Percentages
* kstars: Desktop Planetarium
* ktouch: Touch Typing Tutor
* kturtle: Logo Programming Environment
* kverbos: Study Spanish Verbforms
* kvoctrain: Vocabulary Trainer
* kwordquiz: Vocabulary Trainer

%files
%defattr(-,root,root,-)
%doc COPYING README

##########

%package data
Summary:	Shared data for Trinity educational applications
Group:		System/GUI/Other

%description data
This package contains shared data necessary for running the
educational applications provided with TDE (the Trinity Desktop
Environment).

This package is part of Trinity, as a component of the TDE education module.

%files data
%defattr(-,root,root,-)
%{tde_prefix}/share/applnk/Edutainment/Languages/.directory
%{tde_prefix}/share/applnk/Edutainment/Miscellaneous/.directory
%{tde_prefix}/share/applnk/Edutainment/Mathematics/.directory
%{tde_prefix}/share/applnk/Edutainment/Science/.directory
%{tde_prefix}/share/applnk/Edutainment/Tools/.directory

##########

%package -n trinity-blinken
Summary:	Trinity version of the Simon Says electronic memory game
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-blinken
Blinken is based on an electronic game released in 1978, which
challenges players to remember sequences of increasing length.  On
the face of the device, there are 4 different color buttons, each
with its own distinctive sound.  These buttons light up randomly,
creating the sequence that the player must then recall.  If the
player is successful in remembering the sequence of lights in the
correct order, they advance to the next stage, where an identical
sequence with one extra step is presented.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-blinken
%defattr(-,root,root,-)
%{tde_prefix}/bin/blinken
%{tde_prefix}/share/applications/tde/blinken.desktop
%{tde_prefix}/share/apps/blinken/
%{tde_prefix}/share/config.kcfg/blinken.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/blinken.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/blinken.svgz
%{tde_prefix}/share/doc/tde/HTML/en/blinken/
%{tde_prefix}/share/man/man1/blinken*

##########

%package -n trinity-kalzium
Summary:	Chemistry teaching tool for Trinity
Group:		System/GUI/Other
Requires:	trinity-kalzium-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kalzium
Kalzium is a program which shows you the Periodic System of Elements
(PSE).  You can use Kalzium to search for information about the
elements or to learn facts about the PSE.

Kalzium provides you with all kinds of information about the PSE.
You can look up lots of information about the elements and also use
visualisations to show them.

You can visualise the Periodic Table of the Elements by blocks,
groups, acidic behavior or different states of matter.  You can also
plot data for a range of elements (weight, mean weight, density, IE1,
IE2, electronegativity), and you can go back in time to see what
elements were known at a given date.  In addition, on platforms where
OCaml supports native code generation, Kalzium includes a chemical
equation solver.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kalzium
%defattr(-,root,root,-)
%{tde_prefix}/bin/kalzium
%{tde_prefix}/share/applications/tde/kalzium.desktop
%{tde_prefix}/share/config.kcfg/kalzium.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kalzium.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kalzium.svgz
%{tde_prefix}/share/doc/tde/HTML/en/kalzium/
%{tde_prefix}/share/man/man1/kalzium*

##########

%package -n trinity-kalzium-data
Summary:	Data files for Kalzium
Group:		System/GUI/Other

%description -n trinity-kalzium-data
This package contains architecture-independent data files for
Kalzium, the TDE periodic table application.  This includes pictures
of various chemical equipment and of samples of several elements, in
addition to the actual chemical data.

See the kalzium package for further information.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kalzium-data
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kalzium/

##########

%package -n trinity-kanagram
Summary:	Letter order game for Trinity
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kanagram
KAnagram is a game that is based on the word/letter puzzles that the
author played as a child.  A word is picked at random and displayed
with its letters in a messed order, with difficulty dependent on the
chosen level.  You have an unlimited number of attempts, and scores
are kept.

It is a very simply constructed game, with 3 difficulty levels of
play.  It is fully customizable, allowing you to write in your own
words and set your own 'look and feel' of the game.  It is aimed for
children aged 10+ because of the difficulty, but of course everyone
is welcome to try.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kanagram
%defattr(-,root,root,-)
%{tde_prefix}/bin/kanagram
%{tde_prefix}/share/applications/tde/kanagram.desktop
%{tde_prefix}/share/apps/kanagram/
%{tde_prefix}/share/config.kcfg/kanagram.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kanagram.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kanagram.svgz
%{tde_prefix}/share/doc/tde/HTML/en/kanagram/
%{tde_prefix}/share/man/man1/kanagram*

##########

%package -n trinity-kbruch
Summary:	Fraction calculation teaching tool for Trinity
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kbruch
KBruch is a small program to practice calculating with fractions.
Different exercises are provided for this purpose.  The program
checks the user's input and gives feedback.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kbruch
%defattr(-,root,root,-)
%{tde_prefix}/bin/kbruch
%{tde_prefix}/share/apps/kbruch/
%{tde_prefix}/share/applications/tde/kbruch.desktop
%{tde_prefix}/share/config.kcfg/kbruch.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kbruch.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kbruch.svgz
%{tde_prefix}/share/icons/crystalsvg/*/actions/kbruch_*.png
%{tde_prefix}/share/doc/tde/HTML/en/kbruch/
%{tde_prefix}/share/man/man1/kbruch*

##########

%package -n trinity-keduca
Summary:	Interactive form-based tests for Trinity
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-keduca
KEduca is a flash-card application which allows you to make
interactive form-based tests.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-keduca
%defattr(-,root,root,-)
%{tde_prefix}/bin/keduca
%{tde_prefix}/bin/keducabuilder
%{tde_prefix}/bin/keduca-shrinker
%{tde_prefix}/%{_lib}/trinity/libkeducapart.la
%{tde_prefix}/%{_lib}/trinity/libkeducapart.so
%{tde_prefix}/share/applications/tde/keduca.desktop
%{tde_prefix}/share/applications/tde/keducabuilder.desktop
%{tde_prefix}/share/apps/keduca/
%{tde_prefix}/share/config.kcfg/keduca.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/keduca.png
%{tde_prefix}/share/mimelnk/application/x-edu.desktop
%{tde_prefix}/share/mimelnk/application/x-edugallery.desktop
%{tde_prefix}/share/services/keduca_part.desktop
%{tde_prefix}/share/doc/tde/HTML/en/keduca/
%{tde_prefix}/share/man/man1/keduca*

##########

%package -n trinity-kgeography
Summary:	Geography learning tool for Trinity
Group:		System/GUI/Other
Requires:	trinity-kgeography-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kgeography
KGeography contains maps allowing you to learn various countries or
the political divisions of several countries.  It has several modes,
including a map browser and games involving the names, capitals, or
flags of the map divisions.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kgeography
%defattr(-,root,root,-)
%{tde_prefix}/bin/kgeography
%{tde_prefix}/bin/kgeography_gen_map.pl
%{tde_prefix}/share/applications/tde/kgeography.desktop
%{tde_prefix}/share/config.kcfg/kgeography.kcfg
%{tde_prefix}/share/icons/crystalsvg/*/apps/kgeography.png
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/kgeography.svgz
%{tde_prefix}/share/icons/hicolor/*/apps/kgeography.png
%{tde_prefix}/share/doc/tde/HTML/en/kgeography
%{tde_prefix}/share/man/man1/kgeography*

##########

%package -n trinity-kgeography-data
Summary:	Data files for KGeography
Group:		System/GUI/Other

%description -n trinity-kgeography-data
This package contains architecture-independent data files for
KGeography, the geography learning tool for TDE. This includes map
and flag images.

See the kgeography package for further information.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kgeography-data
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kgeography/

##########

%package -n trinity-khangman
Summary:	The classical hangman game for Trinity
Group:		System/GUI/Other
#Requires:	dustin-dustismo-sans-fonts
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-khangman
KHangMan is a game based on the well known hangman game.  It is aimed
for children aged 6 and above.  It has four levels of difficulty:
Animals (animals words), Easy, Medium and Hard.

A word is picked at random and the letters are hidden.  You must
guess the word by trying one letter after another.  Each time you
guess a wrong letter, a picture of a hangman is drawn.  You must
guess the word before getting hanged!  You have 10 tries.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-khangman
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/khangmanrc
%{tde_prefix}/bin/khangman
%{tde_prefix}/share/applications/tde/khangman.desktop
%{tde_prefix}/share/apps/khangman/
%{tde_prefix}/share/config.kcfg/khangman.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/khangman.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/khangman.svgz
%{tde_prefix}/share/doc/tde/HTML/en/khangman/
%{tde_prefix}/share/man/man1/khangman*

##########

%if %{with kig}
%package -n trinity-kig
Summary:	Interactive geometry program for TDE
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kig
Kig is an application for interactive geometry.  It is intended to
serve two purposes:

- to allow students to interactively explore mathematical figures and
  concepts using the computer;
- to serve as a WYSIWYG tool for drawing mathematical figures and
  including them in other documents.

With this program you can do geometry on a computer just like you
would on a blackboard in a classroom.  However, the program allows
you to move and change parts of a geometrical drawing so that you can
see how the other parts change as a result.

Kig supports loci and user-defined macros.  It also supports imports
and exports to/from foreign file formats including Cabri, Dr. Geo,
KGeo, KSeg and XFig.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kig
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/magic/cabri.magic
%config(noreplace) %{_sysconfdir}/trinity/magic/drgeo.magic
%{tde_prefix}/bin/kig
%{tde_prefix}/bin/pykig.py*
%{tde_prefix}/%{_lib}/trinity/tdefile_drgeo.la
%{tde_prefix}/%{_lib}/trinity/tdefile_drgeo.so
%{tde_prefix}/%{_lib}/trinity/tdefile_kig.la
%{tde_prefix}/%{_lib}/trinity/tdefile_kig.so
%{tde_prefix}/%{_lib}/trinity/libkigpart.la
%{tde_prefix}/%{_lib}/trinity/libkigpart.so
%{tde_prefix}/share/applications/tde/kig.desktop
%{tde_prefix}/share/apps/katepart/syntax/python-kig.xml
%{tde_prefix}/share/apps/kig/
%{tde_prefix}/share/icons/crystalsvg/*/mimetypes/kig_doc.png
%{tde_prefix}/share/icons/crystalsvg/scalable/mimetypes/kig_doc.svgz
%{tde_prefix}/share/icons/hicolor/*/apps/kig.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kig.svgz
%{tde_prefix}/share/mimelnk/application/x-cabri.desktop
%{tde_prefix}/share/mimelnk/application/x-drgeo.desktop
%{tde_prefix}/share/mimelnk/application/x-kig.desktop
%{tde_prefix}/share/mimelnk/application/x-kgeo.desktop
%{tde_prefix}/share/mimelnk/application/x-kseg.desktop
%{tde_prefix}/share/services/tdefile_drgeo.desktop
%{tde_prefix}/share/services/tdefile_kig.desktop
%{tde_prefix}/share/services/kig_part.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kig/
%config(noreplace) %{_sysconfdir}/trinity/magic/cabri.magic.mgc
%config(noreplace) %{_sysconfdir}/trinity/magic/drgeo.magic.mgc
%{tde_prefix}/share/man/man1/kig*
%endif

##########

%package -n trinity-kiten
Summary:	Japanese reference/study tool for Trinity
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}
#Requires:	ttf-kochi-gothic | ttf-kochi-mincho

%description -n trinity-kiten
Kiten is a Japanese reference and study tool for TDE.  It is an
application with multiple functions.  Firstly, it is a convenient
English to Japanese and Japanese to English dictionary.  Secondly, it
is a Kanji dictionary, with multiple ways to look up specific
characters.  Thirdly, it is a tool to help you learn Kanji.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kiten
%defattr(-,root,root,-)
%{tde_prefix}/bin/kiten
%{tde_prefix}/bin/kitengen
%{tde_prefix}/share/applications/tde/kiten.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kiten/
%{tde_prefix}/share/icons/hicolor/*/apps/kiten.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kiten.svgz
%{tde_prefix}/share/man/man1/kiten*

##########

%package -n trinity-klatin
Summary:	Application to help revise/teach Latin
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-klatin
KLatin is a program to help revise Latin.  There are three "sections"
in which different aspects of the language can be revised.  These are
the vocabulary, grammar and verb testing sections.  In addition there
is a set of revision notes that can be used for self-guided revision.

In the vocabulary section an XML file is loaded containing various
words and their local language translations.  KLatin asks you what
each of these words translate into.  The questions take place in a
multiple-choice environment.

In the grammar and verb sections KLatin asks for a particular part of
a noun or a verb, such as the "ablative singular", or the "1st person
indicative passive plural", and is not multiple choice.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-klatin
%defattr(-,root,root,-)
%{tde_prefix}/bin/klatin
%{tde_prefix}/share/applications/tde/klatin.desktop
%{tde_prefix}/share/apps/klatin/
%{tde_prefix}/share/config.kcfg/klatin.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/klatin.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/klatin.svgz
%{tde_prefix}/share/doc/tde/HTML/en/klatin/
%{tde_prefix}/share/man/man1/klatin*

##########

%package -n trinity-klettres
Summary:	Foreign alphabet tutor for Trinity
Group:		System/GUI/Other
Requires:	trinity-klettres-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-klettres
KLettres is an application specially designed to help the user to
learn the alphabet in a new language and then to learn to read simple
syllables.  The user can be a young child aged from two and a half or
an adult that wants to learn the basics of a foreign language.

Seven languages are currently available: Czech, Danish, Dutch,
English, French, Italian and Slovak.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-klettres
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/klettresrc
%{tde_prefix}/bin/klettres
%{tde_prefix}/share/applications/tde/klettres.desktop
%{tde_prefix}/share/config.kcfg/klettres.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/klettres.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/klettres.svgz
%{tde_prefix}/share/doc/tde/HTML/en/klettres/
%{tde_prefix}/share/man/man1/klettres*

##########

%package -n trinity-klettres-data
Summary:	Data files for KLettres foreign alphabet tutor
Group:		System/GUI/Other

%description -n trinity-klettres-data
This package contains architecture-independent data files for
KLettres, the foreign alphabet tutor for TDE.  This includes sound
files and graphics.

See the klettres package for further information.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-klettres-data
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/klettres/

##########

%package -n trinity-kmplot
Summary:	Mathematical function plotter for Trinity
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kmplot
KmPlot is a mathematical function plotter for TDE.  It has a powerful
built-in parser.  You can plot different functions simultaneously and
combine them to build new functions.

KmPlot supports parametric functions and functions in polar
coordinates.  Several grid modes are supported.  Plots may be printed
with high precision in the correct scale.

KmPlot also provides some numerical and visual features, like filling
and calculating the area between the plot and the first axis, finding
maximum and minimum values, changing function parameters dynamically
and plotting derivatives and integral functions.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kmplot
%defattr(-,root,root,-)
%{tde_prefix}/bin/kmplot
%{tde_prefix}/%{_lib}/trinity/libkmplotpart.la
%{tde_prefix}/%{_lib}/trinity/libkmplotpart.so
%{tde_prefix}/share/applications/tde/kmplot.desktop
%{tde_prefix}/share/apps/kmplot/
%{tde_prefix}/share/config.kcfg/kmplot.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kmplot.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kmplot.svgz
%{tde_prefix}/share/mimelnk/application/x-kmplot.desktop
%{tde_prefix}/share/services/kmplot_part.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kmplot/
%{tde_prefix}/share/man/man1/kmplot*

##########

%package -n trinity-kpercentage
Summary:	Percentage calculation teaching tool for Trinity
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kpercentage
KPercentage is a small math application that will help pupils to
improve their skills in calculating percentages.

There is a special training section for the three basic tasks.
Finally the pupil can select a random mode, in which all three tasks
are mixed randomly.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kpercentage
%defattr(-,root,root,-)
%{tde_prefix}/bin/kpercentage
%{tde_prefix}/share/applications/tde/kpercentage.desktop
%{tde_prefix}/share/apps/kpercentage/
%{tde_prefix}/share/icons/hicolor/*/apps/kpercentage.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kpercentage.svgz
%{tde_prefix}/share/doc/tde/HTML/en/kpercentage/
%{tde_prefix}/share/man/man1/kpercentage*

##########

%package -n trinity-kstars
Summary:	Desktop planetarium for Trinity
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kstars-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-indi = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kstars
KStars is a graphical desktop planetarium for TDE.  It depicts an
accurate simulation of the night sky, including stars,
constellations, star clusters, nebulae, galaxies, all planets, the
Sun, the Moon, comets and asteroids.  You can see the sky as it
appears from any location on Earth, on any date.

The user interface is highly intuitive and flexible.  The display can
be panned and zoomed with the mouse, and you can easily identify
objects and track their motion across the sky.  KStars includes many
powerful features, yet the interface is clean and simple and fun to
use.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kstars
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/kstarsrc
%{tde_prefix}/bin/kstars
%{tde_prefix}/share/applications/tde/kstars.desktop
%{tde_prefix}/share/config.kcfg/kstars.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kstars.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kstars.svgz
%{tde_prefix}/share/doc/tde/HTML/en/kstars/
%{tde_prefix}/share/man/man1/kstars*

##########

%package -n trinity-kstars-data
Summary:	Data files for KStars desktop planetarium
Group:		System/GUI/Other

%description -n trinity-kstars-data
This package contains architecture-independent data files for KStars,
the graphical desktop planetarium for TDE.  This includes star
catalogues and astronomical images.

See the kstars package for further information.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kstars-data
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kstars/

##########

%package -n trinity-ktouch
Summary:	Touch typing tutor for Trinity
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-ktouch
KTouch is a program for learning touch typing - it helps you learn to
type on a keyboard quickly and correctly.  Every finger has its place
on the keyboard with associated keys to press.

KTouch helps you learn to touch type by providing you with text to
train on, and adjusts to different levels depending on how good you
are.  It can display which key to press next, and the correct finger
to use.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-ktouch
%defattr(-,root,root,-)
%{tde_prefix}/bin/ktouch
%{tde_prefix}/share/applications/tde/ktouch.desktop
%{tde_prefix}/share/apps/ktouch/
%{tde_prefix}/share/config.kcfg/ktouch.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/ktouch.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/ktouch.svgz
%{tde_prefix}/share/doc/tde/HTML/en/ktouch/
%{tde_prefix}/share/man/man1/ktouch*

##########

%package -n trinity-kturtle
Summary:	Educational Logo programming environment
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kturtle
KTurtle is an educational programming environment using the Logo
programming language.  It tries to make programming as easy and
accessible as possible.  This makes KTurtle suitable for teaching
kids the basics of mathematics, geometry and programming.

The commands used to program are in the style of the Logo programming
language.  The unique feature of Logo is that the commands are often
translated into the speaking language of the programmer.

KTurtle is named after "the turtle" that plays a central role in the
programming environment.  The user programs the turtle, using the
Logo commands, to draw a picture on the canvas.

Note that this version of Logo is only focused on the educational
qualities of the programming language and will not try to suit
professional programmers' needs.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kturtle
%defattr(-,root,root,-)
%{tde_prefix}/bin/kturtle
%{tde_prefix}/share/applications/tde/kturtle.desktop
%{tde_prefix}/share/apps/katepart/syntax/logohighlightstyle*
%{tde_prefix}/share/apps/kturtle/
%{tde_prefix}/share/config.kcfg/kturtle.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kturtle.png
%{tde_prefix}/share/doc/tde/HTML/en/kturtle/
%{tde_prefix}/share/man/man1/kturtle*

##########

%package -n trinity-kverbos
Summary:	Spanish verb form study application for Trinity
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kverbos
Kverbos allows the user to learn the forms of Spanish verbs.  The
program suggests a verb and a time and the user enters the different
verb forms.  The program corrects the user input and gives feedback.

The user can edit the list of the verbs that can be studied.  The
program can build regular verb forms by itself.  Irregular verb forms
have to be entered by the user.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kverbos
%defattr(-,root,root,-)
%{tde_prefix}/bin/kverbos
%{tde_prefix}/share/applications/tde/kverbos.desktop
%{tde_prefix}/share/apps/kverbos/
%{tde_prefix}/share/config.kcfg/kverbos.kcfg
%{tde_prefix}/share/icons/crystalsvg/16x16/actions/kverbosuser.png
%{tde_prefix}/share/icons/hicolor/*/apps/kverbos.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kverbos.svgz
%{tde_prefix}/share/doc/tde/HTML/en/kverbos/
%{tde_prefix}/share/man/man1/kverbos*

##########

%package -n trinity-kvoctrain
Summary:	Vocabulary trainer for Trinity
Group:		System/GUI/Other
Requires:	perl
Requires:	perl-libwww-perl
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kvoctrain
KVocTrain is a little utility to help you train your vocabulary when
you are trying to learn a foreign language.  You can create your own
database with the words you need.  It is intended as a replacement
for index (flash) cards.

You probably remember flashcards from school.  The teacher would
write the original expression on the front side of the card and the
translation on the back.  Then look at the cards one after another.
If you knew the translation, you could put it away.  If you failed,
you put it back to try again.

KVocTrain is not intended to teach you grammar or other sophisticated
things.  This is and probably will stay beyond the scope of this
application.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kvoctrain
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/kvoctrainrc
%{tde_prefix}/bin/kvoctrain
%{tde_prefix}/bin/spotlight2kvtml
%{tde_prefix}/%{_lib}/libkvoctraincore.so.*
%{tde_prefix}/share/applications/tde/kvoctrain.desktop
%{tde_prefix}/share/apps/kvoctrain/
%{tde_prefix}/share/mimelnk/text/x-kvtml.desktop
%{tde_prefix}/share/config.kcfg/kvoctrain.kcfg
%{tde_prefix}/share/config.kcfg/languagesettings.kcfg
%{tde_prefix}/share/config.kcfg/presettings.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kvoctrain.png
%{tde_prefix}/share/doc/tde/HTML/en/kvoctrain/
%{tde_prefix}/share/man/man1/kvoctrain*
%{tde_prefix}/share/man/man1/spotlight2kvtml*

##########

%package -n trinity-kwordquiz
Summary:	Flashcard and vocabulary learning program for Trinity
Group:		System/GUI/Other
Requires:	trinity-tdeedu-data = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-kwordquiz
KWordQuiz is a flashcard-based tool that helps you to master new
vocabularies. It may be a language or any other kind of terminology.

KWordQuiz can open several types of vocabulary data.  Supported are
kvtml files used by other TDE programs such as KVocTrain, wql files
used by WordQuiz for Windows, csv files with comma-separated text,
and xml.gz files created by Pauker (http://pauker.sourceforge.net).

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-kwordquiz
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/kwordquizrc
%{tde_prefix}/bin/kwordquiz
%{tde_prefix}/share/applications/tde/kwordquiz.desktop
%{tde_prefix}/share/apps/kwordquiz/
%{tde_prefix}/share/config.kcfg/kwordquiz.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kwordquiz.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kwordquiz.svg
%{tde_prefix}/share/icons/crystalsvg/*/mimetypes/kwordquiz_doc.png
%{tde_prefix}/share/icons/crystalsvg/scalable/mimetypes/kwordquiz_doc.svg
%{tde_prefix}/share/mimelnk/application/x-kwordquiz.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kwordquiz/
%{tde_prefix}/share/man/man1/kwordquiz*
%{tde_prefix}/share/man/man1/langen*

##########

%package -n trinity-libtdeedu3
Summary:	Library for use with Trinity educational apps
Group:		System/GUI/Other

%description -n trinity-libtdeedu3
The TDE-based library libtdeedu is used with educational
applications.  It currently provides support for data plotting and
vocabulary items (including a parser for kvtml vocabulary files).

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-libtdeedu3
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libextdate.so.*
%{tde_prefix}/%{_lib}/libtdeeducore.so.*
%{tde_prefix}/%{_lib}/libtdeeduplot.so.*
%{tde_prefix}/%{_lib}/libtdeeduui.so.*

##########

%package -n trinity-libtdeedu-devel
Summary:	Development files for Trinity educational library
Group:		Development/Libraries/Other
Requires:	trinity-libtdeedu3 = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-libtdeedu-devel
The TDE-based library libtdeedu is used with educational
applications.  It currently provides support for data plotting and
vocabulary items (including a parser for kvtml vocabulary files).

Development files for libtdeedu are included in this package.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-libtdeedu-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/libtdeedu/
%{tde_prefix}/%{_lib}/libextdate.la
%{tde_prefix}/%{_lib}/libextdate.so
%{tde_prefix}/%{_lib}/libtdeeducore.la
%{tde_prefix}/%{_lib}/libtdeeducore.so
%{tde_prefix}/%{_lib}/libtdeeduui.la
%{tde_prefix}/%{_lib}/libtdeeduui.so
%{tde_prefix}/%{_lib}/libtdeeduplot.la
%{tde_prefix}/%{_lib}/libtdeeduplot.so

##########

%package -n trinity-libkiten1
Summary:	Library for Kiten Japanese reference/study tool
Group:		System/GUI/Other
#Requires:	kanjidic

%description -n trinity-libkiten1
Kiten is a Japanese reference/study tool for TDE.  The library
libkiten contains portions of Kiten that may be useful for other
applications.  These portions include dictionary, character lookup
and widget classes.

This package contains the libkiten library along with supporting
data, such as Japanese language data files and GUI resource files.
For further information, see the kiten package.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-libkiten1
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkiten.so.*
%{tde_prefix}/share/apps/kiten/
%{tde_prefix}/share/config.kcfg/kiten.kcfg
%{tde_prefix}/share/icons/crystalsvg/16x16/actions/kanjidic.png
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/edit_add.png
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/edit_remove.png
%{tde_prefix}/share/icons/crystalsvg/22x22/actions/kanjidic.png
%{tde_prefix}/share/icons/locolor/16x16/actions/edit_add.png
%{tde_prefix}/share/icons/locolor/16x16/actions/edit_remove.png

##########

%package -n trinity-libkiten-devel
Summary:	Development files for Kiten library
Group:		Development/Libraries/Other
Requires:	trinity-libkiten1 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdelibs-devel >= %{version}

%description -n trinity-libkiten-devel
Kiten is a Japanese reference/study tool for TDE.  The library
libkiten contains portions of Kiten that may be useful for other
applications.  These portions include dictionary, character lookup
and widget classes.

Development files for libkiten are included in this package.  For
further information, see the kiten package.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-libkiten-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/libkiten/
%{tde_prefix}/%{_lib}/libkiten.la
%{tde_prefix}/%{_lib}/libkiten.so

##########

%package -n trinity-indi
Summary:	Instrument Neutral Distributed Interface for astronomical devices
Group:		System/GUI/Other

%description -n trinity-indi
INDI is an Instrument Neutral Distributed Interface control protocol for
astronomical devices, which provides a framework that decouples low level
hardware drivers from high level front end clients. Clients that use the
device drivers are completely unaware of the device capabilities and
communicate with the device drivers and build a completely dynamic GUI
based on the services provided by the device.

This package is part of Trinity, as a component of the TDE education module.

%files -n trinity-indi
%defattr(-,root,root,-)
%{tde_prefix}/bin/apmount
%{tde_prefix}/bin/apogee_ppi
%{tde_prefix}/bin/celestrongps
%{tde_prefix}/bin/fliccd
%{tde_prefix}/bin/fliwheel
%{tde_prefix}/bin/indiserver
%{tde_prefix}/bin/lx200_16
%{tde_prefix}/bin/lx200autostar
%{tde_prefix}/bin/lx200basic
%{tde_prefix}/bin/lx200classic
%{tde_prefix}/bin/lx200generic
%{tde_prefix}/bin/lx200gps
%{tde_prefix}/bin/sbigccd
%{tde_prefix}/bin/skycommander
%{tde_prefix}/bin/temma
%if %{with v4l}
%{tde_prefix}/bin/meade_lpi
%{tde_prefix}/bin/v4ldriver
%{tde_prefix}/bin/v4lphilips
%endif
%{tde_prefix}/share/man/man1/celestrongps*
%{tde_prefix}/share/man/man1/fliccd*
%{tde_prefix}/share/man/man1/indi*
%{tde_prefix}/share/man/man1/lx200*
%{tde_prefix}/share/man/man1/temma*
%{tde_prefix}/share/man/man1/v4l*

##########

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries/Other
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libtdeedu-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-libkiten-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdeedu-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdeedu-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the development files for tdeedu.

%files devel
%defattr(-,root,root,-)
%doc libtdeedu/AUTHORS libtdeedu/README
# kstars
%{tde_prefix}/include/tde/kstarsinterface.h
%{tde_prefix}/include/tde/simclockinterface.h
# kvoctrain
%{tde_prefix}/%{_lib}/libkvoctraincore.la
%{tde_prefix}/%{_lib}/libkvoctraincore.so


%conf -p
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"


%install -a

# Links duplicate files
%fdupes "%{?buildroot}%{tde_prefix}/share"

