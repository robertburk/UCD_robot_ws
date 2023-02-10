// Auto-generated. Do not edit!

// (in-package ucd_robot.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class DataState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.bias_state = null;
      this.buffer_state = null;
    }
    else {
      if (initObj.hasOwnProperty('bias_state')) {
        this.bias_state = initObj.bias_state
      }
      else {
        this.bias_state = false;
      }
      if (initObj.hasOwnProperty('buffer_state')) {
        this.buffer_state = initObj.buffer_state
      }
      else {
        this.buffer_state = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DataState
    // Serialize message field [bias_state]
    bufferOffset = _serializer.bool(obj.bias_state, buffer, bufferOffset);
    // Serialize message field [buffer_state]
    bufferOffset = _serializer.bool(obj.buffer_state, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DataState
    let len;
    let data = new DataState(null);
    // Deserialize message field [bias_state]
    data.bias_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [buffer_state]
    data.buffer_state = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 2;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ucd_robot/DataState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e4df093d868adffe6bda0f3e2ebd1f68';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool bias_state
    bool buffer_state
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DataState(null);
    if (msg.bias_state !== undefined) {
      resolved.bias_state = msg.bias_state;
    }
    else {
      resolved.bias_state = false
    }

    if (msg.buffer_state !== undefined) {
      resolved.buffer_state = msg.buffer_state;
    }
    else {
      resolved.buffer_state = false
    }

    return resolved;
    }
};

module.exports = DataState;
