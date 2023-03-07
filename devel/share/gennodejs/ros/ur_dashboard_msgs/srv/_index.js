
"use strict";

let GetLoadedProgram = require('./GetLoadedProgram.js')
let IsProgramSaved = require('./IsProgramSaved.js')
let AddToLog = require('./AddToLog.js')
let GetSafetyMode = require('./GetSafetyMode.js')
let GetProgramState = require('./GetProgramState.js')
let Load = require('./Load.js')
let IsProgramRunning = require('./IsProgramRunning.js')
let RawRequest = require('./RawRequest.js')
let GetRobotMode = require('./GetRobotMode.js')
let Popup = require('./Popup.js')
let IsInRemoteControl = require('./IsInRemoteControl.js')

module.exports = {
  GetLoadedProgram: GetLoadedProgram,
  IsProgramSaved: IsProgramSaved,
  AddToLog: AddToLog,
  GetSafetyMode: GetSafetyMode,
  GetProgramState: GetProgramState,
  Load: Load,
  IsProgramRunning: IsProgramRunning,
  RawRequest: RawRequest,
  GetRobotMode: GetRobotMode,
  Popup: Popup,
  IsInRemoteControl: IsInRemoteControl,
};
