import pytest
import time

from fe.access import goods
from fe import conf


@pytest.mark.parametrize(
    "merchantname",
    [
        "test_getmerchantgoods1_{}".format(time.time()),
        "test_getmerchantgoods2_{}".format(time.time()),
        "test_getmerchantgoods3_{}".format(time.time()),
    ],
    "merchantname"
)

def test_getmerchantgoods(merchantname: str):
    m = merchant.Merchant(conf.URL)
    # register a merchant

    password = "password_" + username
    terminal = "terminal_" + username

    assert a.register(username, password)

    # search right
    login_ok, token = m.login(username, password, terminal)
    assert login_ok

    # search wrong merchantname
    login_ok, token = m.login(username + "xxx", password, terminal)
    assert not login_ok
