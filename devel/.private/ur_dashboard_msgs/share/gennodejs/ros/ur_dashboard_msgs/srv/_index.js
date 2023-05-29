
"use strict";

let GetProgramState = require('./GetProgramState.js')
let IsProgramSaved = require('./IsProgramSaved.js')
let GetLoadedProgram = require('./GetLoadedProgram.js')
let Popup = require('./Popup.js')
let RawRequest = require('./RawRequest.js')
let GetRobotMode = require('./GetRobotMode.js')
let AddToLog = require('./AddToLog.js')
let GetSafetyMode = require('./GetSafetyMode.js')
let IsInRemoteControl = require('./IsInRemoteControl.js')
let IsProgramRunning = require('./IsProgramRunning.js')
let Load = require('./Load.js')

module.exports = {
  GetProgramState: GetProgramState,
  IsProgramSaved: IsProgramSaved,
  GetLoadedProgram: GetLoadedProgram,
  Popup: Popup,
  RawRequest: RawRequest,
  GetRobotMode: GetRobotMode,
  AddToLog: AddToLog,
  GetSafetyMode: GetSafetyMode,
  IsInRemoteControl: IsInRemoteControl,
  IsProgramRunning: IsProgramRunning,
  Load: Load,
};
