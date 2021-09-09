A simple and easy to use database using JSON.

__Setup:__

1. First, use the following import: from qikdb import DB
2. Then, create a new instance of the "DB" class.
3. In the class constructor/initializer put a new object like so: config = {}

(Config dictionary/object params:

"name" - Defines database name.)

__Usage:__

"all" - Takes no params, returns all keys in the database.

"get" - Takes one param (key) returns value of given key.

"set" - Takes two params (key), and (data) sets a key's value in the database (overwrites any pre-existing values in key).

"delete" - Takes one param (key) deletes given key from the database (Note: if "all" is given as the key, all keys will be deleted from the database.

"add" - Takes two params (key), and (data) adds given data to key's current value (Note: both the key's value, and the data must be type int).

"subtract" - Takes two params (key), and (data) subtracts given data from key's current value (Note: both key's value, and the data must be type int).

"unlink" - Takes no params, deletes all keys, and database's file.
