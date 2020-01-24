# Create a GIS Application using Flask, Stadia Maps, and MongoDB

This guide will use Stadia Maps free tier plan and [hosted vector map tiles](https://stadiamaps.com/products/map-tiles/) to create a GIS web app using Flask. Your Flask application will use a MongoDB database to store [GeoJSON](https://tools.ietf.org/html/rfc7946) data to display as markers on your Stadia Map powered map. GeoJson is a format for encoding a variety of geographic data structures based on JavaScript Object Notation (JSON).

The GeoJSON data that you will use is a subset of [Philadelphia's Street Tree Inventory](https://www.opendataphilly.org/dataset/philadelphia-street-tree-inventory) dataset. Since the entire dataset is very large, a subset was used to keep this example simple and to reduce MongoDB storage requirements. When you are finished with this guide, you will have a Stadia Maps powered map with markers displaying the location of the trees that surround Linode's headquarters in Philadelphia, USA.

While the example in this guide is simple, its components can be adopted to build a GIS app that maps any data you would like to display to your users.

The sections in this guide will cover the following topics:

- Setting up your development environment
- Starting a local MongoDB instance and importing a data set to your database
- Creating a Flask app that uses Stadia Maps to display your GeoJSON data as markers on your map.

    {{< note >}}
This guide assumes a basic familiarity with programming concepts, Python, HTML, CSS, and JavaScript.
    {{</ note >}}

