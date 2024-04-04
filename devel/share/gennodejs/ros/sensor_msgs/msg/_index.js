
"use strict";

let RelativeHumidity = require('./RelativeHumidity.js');
let Range = require('./Range.js');
let Joy = require('./Joy.js');
let PointField = require('./PointField.js');
let PointCloud = require('./PointCloud.js');
let Image = require('./Image.js');
let LaserEcho = require('./LaserEcho.js');
let MultiEchoLaserScan = require('./MultiEchoLaserScan.js');
let TimeReference = require('./TimeReference.js');
let JointState = require('./JointState.js');
let FluidPressure = require('./FluidPressure.js');
let CompressedImage = require('./CompressedImage.js');
let Imu = require('./Imu.js');
let MultiDOFJointState = require('./MultiDOFJointState.js');
let JoyFeedback = require('./JoyFeedback.js');
let ChannelFloat32 = require('./ChannelFloat32.js');
let PointCloud2 = require('./PointCloud2.js');
let RegionOfInterest = require('./RegionOfInterest.js');
let JoyFeedbackArray = require('./JoyFeedbackArray.js');
let NavSatStatus = require('./NavSatStatus.js');
let LaserScan = require('./LaserScan.js');
let Temperature = require('./Temperature.js');
let BatteryState = require('./BatteryState.js');
let MagneticField = require('./MagneticField.js');
let NavSatFix = require('./NavSatFix.js');
let CameraInfo = require('./CameraInfo.js');
let Illuminance = require('./Illuminance.js');

module.exports = {
  RelativeHumidity: RelativeHumidity,
  Range: Range,
  Joy: Joy,
  PointField: PointField,
  PointCloud: PointCloud,
  Image: Image,
  LaserEcho: LaserEcho,
  MultiEchoLaserScan: MultiEchoLaserScan,
  TimeReference: TimeReference,
  JointState: JointState,
  FluidPressure: FluidPressure,
  CompressedImage: CompressedImage,
  Imu: Imu,
  MultiDOFJointState: MultiDOFJointState,
  JoyFeedback: JoyFeedback,
  ChannelFloat32: ChannelFloat32,
  PointCloud2: PointCloud2,
  RegionOfInterest: RegionOfInterest,
  JoyFeedbackArray: JoyFeedbackArray,
  NavSatStatus: NavSatStatus,
  LaserScan: LaserScan,
  Temperature: Temperature,
  BatteryState: BatteryState,
  MagneticField: MagneticField,
  NavSatFix: NavSatFix,
  CameraInfo: CameraInfo,
  Illuminance: Illuminance,
};
