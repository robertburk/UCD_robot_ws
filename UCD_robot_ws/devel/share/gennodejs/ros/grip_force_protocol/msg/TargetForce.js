// Auto-generated. Do not edit!

// (in-package grip_force_protocol.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class TargetForce {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.target_force = null;
    }
    else {
      if (initObj.hasOwnProperty('target_force')) {
        this.target_force = initObj.target_force
      }
      else {
        this.target_force = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TargetForce
    // Serialize message field [target_force]
    bufferOffset = _serializer.float32(obj.target_force, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TargetForce
    let len;
    let data = new TargetForce(null);
    // Deserialize message field [target_force]
    data.target_force = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'grip_force_protocol/TargetForce';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e0e0e39f568c9ce1104c278640a8f08d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 target_force
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TargetForce(null);
    if (msg.target_force !== undefined) {
      resolved.target_force = msg.target_force;
    }
    else {
      resolved.target_force = 0.0
    }

    return resolved;
    }
};

module.exports = TargetForce;
