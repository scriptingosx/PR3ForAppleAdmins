#!/usr/bin/swift -swift-version 4

import Foundation

let encoder = PropertyListEncoder()
encoder.outputFormat = .xml // .xml or .binary 

let berry = [ "fruit": "Blueberry", "size": "small", "color": "blue" ]
let berryURL = URL(fileURLWithPath: "blueberry.plist")

do {
  let data = try encoder.encode(berry)
  try data.write(to: berryURL)
} catch {
  // Handle error
  print(error)
}

let everyBoolean = [ true, false ]
let booleanURL = URL(fileURLWithPath: "everyBoolean.plist")

do {
  let data = try encoder.encode(everyBoolean)
  try data.write(to: booleanURL)
} catch {
  // Handle error
  print(error)
}
