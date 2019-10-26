# -----------------------------------------------------------------------------
# Copyright (C) 2019 Xinyu Ma
#
# This file is part of python-ndn.
#
# python-ndn is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-ndn is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with python-ndn.  If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------
from typing import Optional
from ndn.app import NDNApp
from ndn.encoding import Name, InterestParam, BinaryStr, FormalName, MetaInfo
import logging


logging.basicConfig(format='[{asctime}]{levelname}:{message}',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    style='{')


app = NDNApp()


@app.route('/example/rpc')
def on_interest(name: FormalName, param: InterestParam, app_param: Optional[BinaryStr]):
    app_param = bytes(app_param)
    print(f'>> I: {Name.to_str(name)}, {param}, {app_param}')
    if not app_param:
        print("<< No application parameter, dropped")
        return
    s = sum(int(x) for x in app_param.split())
    content = str(s).encode()
    app.put_data(name, content=content, freshness_period=500)
    print(f'<< D: {Name.to_str(name)}')
    print(MetaInfo(freshness_period=500))
    print(f'Content: {content}')
    print('')


if __name__ == '__main__':
    app.run_forever()
