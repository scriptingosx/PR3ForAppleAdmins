#!/usr/bin/swift -swift-version 4

import Foundation

// replace this with your path to the sample files
let samplePath = "../examples"
let dictPath = "\(samplePath)/berry.plist"
let dictURL = URL(fileURLWithPath: dictPath)

let decoder = PropertyListDecoder()

if let dictData = try? Data(contentsOf: dictURL) {
    if let sampleDict = try? decoder.decode(Dictionary<String,String>.self, from: dictData) {
        for (key, value) in sampleDict {
            print("\(key) = \(value)")
        }
    }
} else {
    print("couldn't read: \(dictPath)")
}

print()

// replace this with your path to the sample files
let arrayPath = "\(samplePath)/list.plist"
let arrayURL = URL(fileURLWithPath: arrayPath)
if let arrayData = try? Data(contentsOf:arrayURL){
    if let sampleArray = try? decoder.decode(Array<String>.self, from: arrayData) {
        for (index, value) in sampleArray.enumerated() {
            print("\(index): \(value)")
        }
    }
} else {
    print("couldn't read: \(arrayPath)")
}


