# Project 2 README
## Overview
Project 2 for CSE 331 F23 is an implementation of browser history using a doubly linked list (DLL). The project involves creating and manipulating a DLL to simulate the behavior of a web browser's history feature.

## Features
Node: A fundamental doubly linked list node class.<br />
DLL (Doubly Linked List): Implementation of a doubly linked list with essential operations such as insertion, deletion, searching, and reversing.<br />
BrowserHistory: A class that simulates a web browser's history using a DLL, allowing navigation through web pages visited.<br />
Malicious URL Filtering: Integration with a simulated metrics API to filter out malicious URLs from browser history navigation.<br />
## Usage
DLL Operations:<br />
push: Add a node to the front or back of the list.<br />
pop: Remove a node from the front or back of the list.<br />
list_to_dll / dll_to_list: Convert between Python list and DLL.<br<br /> />
find / find_all: Search for nodes with a specific value.<br />
remove / remove_all: Remove nodes with a specific value.<br />
reverse: Reverse the order of nodes in the list.<br />
BrowserHistory:<br />
visit: Add a new URL to the browser history.<br />
backward / forward: Navigate backward or forward through the browser history.<br />
get_current_url: Retrieve the current URL in the browser history.<br />Installation
No special installation is required beyond Python 3.7 or newer.

## Dependencies
Python 3.7+

## Author
Dallas Foley

