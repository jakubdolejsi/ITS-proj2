ITS - project 1: BDD scenarios
==============================

author: Jakub Dolejší (xdolej09)\
testing platform: OpenCart \
URL: http://mys01.fit.vutbr.cz:8014/ \
testing target: product purchasing process

Introduction
----------

Aim of this project was to create BDD scenarios for testing OpenCart
e-commerce platform.

Product choosing (product\_choose.feature)
----------------------------------------------

This file contains tests of searching product and choosing product.

Side actions with product (product\_action.feature)
--------------------------------------------------------

This file tests behavior of product side actions such as comparing
products and adding product to wish-list.

Action with account (account\_action.feature)
----------------------------------------
This file tests the most important actions with account, concretely
creating new account, logging into the existing account and logout.
 

Product cart (product\_cart.feature)
----------------------------------------

This file contains work with concrete product such as adding,
deleting or updating item in cart.

Product buying (product\_purchase.feature)
-----------------------------------------

This file contains tests of process of purchasing new product, including payment
and delivery.