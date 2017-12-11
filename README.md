# nevra-resolver

web service to parse nevra and return json

# Deployment

```bash
oc new-build --strategy docker --name nevra-resolver .
oc start-build  nevra-resolver --from-dir .
oc new-app nevra-resolver
oc expose service newra-resolver

```

## Copyright

Copyright (C) 2017 Red Hat Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

The GNU General Public License is provided within the file LICENSE.
