# Micro-CMS v1

### Problem

You are presented with a micro CMS that allows you to make new pages. 

### Solution

There are several solutions:

- One is to create a XSS with the title, i.e. `<IMG SRC=javascript:alert(&quot;XSS&quot;)>`.
- One is to search for a secret page based on the numberings. Adding `/edit/` before the page number lets you edit the page and find a flag.
- One is to add a onclick() event, i.e. `<button onclick=alert('hello')>Some button</button>`. If you inspect element, you will find that the button has a flag.
