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

class SystemState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.system_state = null;
      this.sensor_state = null;
      this.gripper_state = null;
      this.robot_state = null;
      this.camera_state = null;
    }
    else {
      if (initObj.hasOwnProperty('system_state')) {
        this.system_state = initObj.system_state
      }
      else {
        this.system_state = false;
      }
      if (initObj.hasOwnProperty('sensor_state')) {
        this.sensor_state = initObj.sensor_state
      }
      else {
        this.sensor_state = false;
      }
      if (initObj.hasOwnProperty('gripper_state')) {
        this.gripper_state = initObj.gripper_state
      }
      else {
        this.gripper_state = false;
      }
      if (initObj.hasOwnProperty('robot_state')) {
        this.robot_state = initObj.robot_state
      }
      else {
        this.robot_state = false;
      }
      if (initObj.hasOwnProperty('camera_state')) {
        this.camera_state = initObj.camera_state
      }
      else {
        this.camera_state = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SystemState
    // Serialize message field [system_state]
    bufferOffset = _serializer.bool(obj.system_state, buffer, bufferOffset);
    // Serialize message field [sensor_state]
    bufferOffset = _serializer.bool(obj.sensor_state, buffer, bufferOffset);
    // Serialize message field [gripper_state]
    bufferOffset = _serializer.bool(obj.gripper_state, buffer, bufferOffset);
    // Serialize message field [robot_state]
    bufferOffset = _serializer.bool(obj.robot_state, buffer, bufferOffset);
    // Serialize message field [camera_state]
    bufferOffset = _serializer.bool(obj.camera_state, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SystemState
    let len;
    let data = new SystemState(null);
    // Deserialize message field [system_state]
    data.system_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [sensor_state]
    data.sensor_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [gripper_state]
    data.gripper_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [robot_state]
    data.robot_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [camera_state]
    data.camera_state = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ucd_robot/SystemState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '13c814d1fd4a9cbdec20374044113342';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool system_state 
    bool sensor_state
    bool gripper_state
    bool robot_state
    bool camera_state
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SystemState(null);
    if (msg.system_state !== undefined) {
      resolved.system_state = msg.system_state;
    }
    else {
      resolved.system_state = false
    }

    if (msg.sensor_state !== undefined) {
      resolved.sensor_state = msg.sensor_state;
    }
    else {
      resolved.sensor_state = false
    }

    if (msg.gripper_state !== undefined) {
      resolved.gripper_state = msg.gripper_state;
    }
    else {
      resolved.gripper_state = false
    }

    if (msg.robot_state !== undefined) {
      resolved.robot_state = msg.robot_state;
    }
    else {
      resolved.robot_state = false
    }

    if (msg.camera_state !== undefined) {
      resolved.camera_state = msg.camera_state;
    }
    else {
      resolved.camera_state = false
    }

    return resolved;
    }
};

module.exports = SystemState;
