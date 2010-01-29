#! /usr/bin/perl -w
#
# --- BEGIN COPYRIGHT BLOCK ---
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation;
# version 2.1 of the License.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301  USA 
# 
# Copyright (C) 2007 Red Hat, Inc.
# All rights reserved.
# --- END COPYRIGHT BLOCK ---
#

use CGI;

[REQUIRE_CFG_PL]


my $host = get_host();
my $secure_port = get_secure_port();
my $port = get_port();

my $q = new CGI;

sub DoPage
{

  my $error = $q->param('error');

  open(FILE, "< welcome.html");

  print $q->header();

  while ($l = <FILE>)
  {
      $l =~ s/\$error/$error/g;
      $l =~ s/\$host/$host/g;
      $l =~ s/\$secure_port/$secure_port/g;
      $l =~ s/\$port/$port/g;
      print $l;
  }

  close(FILE);
}

&DoPage(); 
