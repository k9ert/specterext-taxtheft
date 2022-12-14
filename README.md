# Overview

This is a Specter Extension to help to calculate tax obligation. It's work in progress and there is not yet much to see. The plan is:
* Being able to obtain and store/cache fiat prices for bitcoin in various fiat currencies
* Create a model where an incoming transaction is considered to be an "investment" from a tax point of view and an outgoing Tx a "sell off" and therefore a taxable event.
* The calculation of the "gain" is the basis of the taxation. So this should be possible with a click of a button for every outgoing transaction. 
* Following UTXOs and Transactions in order to automatically calculate the "purchase price" for the amount which is currently spent is the main task of this extension
* A FIFO model is currenty in scope, only.

# How to get it to run

After creation, you can get the extension to run like this in your
  development environment:
      
      virtualenv --python=python3 .env
      . ./.env/bin/activate
      pip3 install -e .
      python3 -m cryptoadvance.specter server --config DevelopmentConfig --debug
      # Point your browser to http://localhost:25441
      # Click "Choose plugins" --> YourExtension

  However, there is still not much to see yet. So maybe you want to run the tests:

      pytest

  If you want to package it, you can build it like this:

      python3 -m pip install --upgrade build
      python3 -m build
      # Install it like this:
      pip3 install dist/YourOrg_YourId-0.0.1-py3-none-any.whl

  If you want to bring your extension to production, please refer to the
  readme in the dummy-extension repo:
  https://github.com/cryptoadvance/specterext-dummy#how-to-get-this-to-
  production

  To publish your package:

      python3 -m pip install --upgrade twine
      python3 -m twine upload --repository testpypi dist/*