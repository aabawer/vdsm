# Copyright 2020 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
#

# Re-export public API
from .api import generate_state
from .api import is_autoconf_enabled
from .api import is_dhcp_enabled
from .api import is_nmstate_backend
from .api import setup
from .api import show_interfaces
from .api import show_nameservers

# Re-export nmstate schema
from .schema import BondSchema
from .schema import DNS
from .schema import Interface
from .schema import InterfaceIP
from .schema import InterfaceIPv6
from .schema import InterfaceState
from .schema import InterfaceType
from .schema import LinuxBridge
from .schema import OvsBridgeSchema
from .schema import Route


__all__ = [
    'generate_state',
    'is_autoconf_enabled',
    'is_dhcp_enabled',
    'is_nmstate_backend',
    'setup',
    'show_interfaces',
    'show_nameservers',
    'BondSchema',
    'DNS',
    'Interface',
    'InterfaceIP',
    'InterfaceIPv6',
    'InterfaceState',
    'InterfaceType',
    'LinuxBridge',
    'OvsBridgeSchema',
    'Route',
]
