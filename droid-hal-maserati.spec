# These and other macros are documented in dhd/droid-hal-device.inc
%define device maserati
%define vendor motorola
%define vendor_pretty Motorola
%define device_pretty Droid 4
%define installable_zip 1
%define makefstab_skip_entries /tmp /system

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc
