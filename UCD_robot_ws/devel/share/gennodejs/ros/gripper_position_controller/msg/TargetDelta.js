// Auto-generated. Do not edit!

// (in-package gripper_position_controller.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class TargetDelta {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.target_delta = null;
    }
    else {
      if (initObj.hasOwnProperty('target_delta')) {
        this.target_delta = initObj.target_delta
      }
      else {
        this.target_delta = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TargetDelta
    // Serialize message field [target_delta]
    bufferOffset = _serializer.float32(obj.target_delta, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TargetDelta
    let len;
    let data = new TargetDelta(null);
    // Deserialize message field [target_delta]
    data.target_delta = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'gripper_position_controller/TargetDelta';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7f44729b36d41b3490ff1e46feb4d3a0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 target_delta
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TargetDelta(null);
    if (msg.target_delta !== undefined) {
      resolved.target_delta = msg.target_delta;
    }
    else {
      resolved.target_delta = 0.0
    }

    return resolved;
    }
};

module.exports = TargetDelta;
