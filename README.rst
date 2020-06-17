
API for Royal Belgian Football Association


=======
Install
=======

.. code-block:: bash

    pip install acff

=======
Example
=======

.. code-block:: python

    from acff.client import Acff

    sha256Hash = 'e882264b79eaabb7f66f94101fc81921565fa9496ea0c9604e8c6115b83a527a'
    client = Acff(sha256Hash)
    result = client.operation_name({
        'channel': 'acff',
        'language': 'en'
    })
    result = client.get_legal_navigation_for_channel({
        'clubId': '2248',
        'language': 'en'
    })


=======
Donation
=======

.. image:: https://img.shields.io/badge/Donate-PayPal-green.svg
  :target: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YYZQ6ZRZ3EW5C
