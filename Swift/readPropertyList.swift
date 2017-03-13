#!/usr/bin/swift

import Foundation

// replace this with your path to the sample files
let samplePath = "../examples"

let dictPath = "\(samplePath)/berry.plist"
// casting to [String: AnyObject] ist not mandatory but probably safer
if let sampleDict = NSDictionary(contentsOfFile: dictPath) as? [String: AnyObject] {
    for (key, value) in sampleDict {
        print("\(key) = \(value)")
    }
} else {
    print("couldn't read: \(dictPath)")
}

print()

// replace this with your path to the sample files
let arrayPath = "\(samplePath)/list.plist"
// casting to [AnyObject] ist not mandatory but probably safer
if let sampleArray = NSArray(contentsOfFile: arrayPath) as? [AnyObject] {
    for (index, value) in sampleArray.enumerated() {
        print("\(index): \(value)")
    }
} else {
    print("couldn't read: \(arrayPath)")
}
