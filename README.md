# flask-simple

SimpleDB integration for Flask.


![Turtle Sketch][]


## Meta

- Author: Randall Degges
- Email: r@rdegges.com
- Site: http://www.rdegges.com
- Status: maintained, active


## Purpose

I love using Amazon's [SimpleDB][] database -- it's drop-dead simple, fun to
use, and makes storing data incredibly enjoyable.

SimpleDB is a NoSQL database, 100% hosted by Amazon, which allows you to store
any variable JSON data.  All fields are indexed automatically, so no table
schema is necessary -- and the best part is that you can query records via SQL.

It's great for storing log data, crawler data, and essentially any information
where you might do a lot of writes, but not necessarily need extremely fast
reads.

I've been using it for for quite a while now, and can't recommend it enough.

The only problem I had using SimpleDB with Flask is lack of an official
extension -- so I created one!

This extension makes working with SimpleDB in Flask projects simple and
painless -- and doesn't get in your way at all (*no need to compromise!*).


## Documentation

All project documentation is hosted at ReadTheDocs:
http://flask-simple.readthedocs.org/en/latest/


  [Turtle Sketch]: https://github.com/rdegges/flask-simple/raw/master/assets/turtle-sketch.jpg "Turtle Sketch"
  [SimpleDB]: http://aws.amazon.com/simpledb/ "SimpleDB"
