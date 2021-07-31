# clictune2invites

### Setup

`pip install -r requirements.txt`

**You will need Burp to get your session cookie**

[Tutorial for setting up Burp](https://portswigger.net/burp/documentation/desktop/getting-started/proxy-setup/browser)

When you got Burp configured correctly, you can login in your clictune account and start the proxy of Burp and reload the page.

You will see in the headers of the http request something like that:
`ci_session=ad0e6aefcc4c17c658638d4e4d45e13614c3171e`

Copy that, and you can continues :)

### How it works

The script send a request with your session and fetch all invites you want !
