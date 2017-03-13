#!/usr/bin/swift

import Foundation

let berry:NSDictionary = [ "fruit": "Blueberry", "size": "small", "color": "blue" ]

berry.write(toFile: "blueberry.plist", atomically: true)

let everyBoolean:NSArray = [ true, false ]

everyBoolean.write(toFile: "everyBoolean.plist", atomically: true)
