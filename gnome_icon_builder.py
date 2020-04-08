#!/usr/bin/python3
#
"""
Shared tools for building packages
"""
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#


# stdlib
import configparser
import os
import subprocess
import sys
import xml.sax
import pathlib


def prepare_data_files(theme_index_path):
	data_files = []
	
	theme_content_root = pathlib.Path(theme_index_path).parent
	
	parser = configparser.ConfigParser()
	parser.read(theme_index_path)
	
	directories = parser.get("Icon Theme", "Directories").split(",")
	
	for directory in directories:
		if directory:
			base_path = theme_content_root
			for element in directory.split("/"):
				open(base_path / element / "__init__.py", "w").close()
				base_path = base_path / element
			
			abs_dir_path = (theme_content_root / directory).relative_to(os.getcwd())
			
			data_files += [str(abs_dir_path / x) for x in os.listdir(abs_dir_path)]
	
	return data_files