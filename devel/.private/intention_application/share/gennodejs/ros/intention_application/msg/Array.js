// Auto-generated. Do not edit!

// (in-package intention_application.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Array {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x = null;
      this.y = null;
      this.intention = null;
    }
    else {
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0;
      }
      if (initObj.hasOwnProperty('intention')) {
        this.intention = initObj.intention
      }
      else {
        this.intention = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Array
    // Serialize message field [x]
    bufferOffset = _serializer.int32(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.int32(obj.y, buffer, bufferOffset);
    // Serialize message field [intention]
    bufferOffset = _serializer.bool(obj.intention, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Array
    let len;
    let data = new Array(null);
    // Deserialize message field [x]
    data.x = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [intention]
    data.intention = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'intention_application/Array';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd6d4ea0cfc5344e240c5b9bd523fcbef';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 x
    int32 y
    bool intention
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Array(null);
    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0
    }

    if (msg.intention !== undefined) {
      resolved.intention = msg.intention;
    }
    else {
      resolved.intention = false
    }

    return resolved;
    }
};

module.exports = Array;
