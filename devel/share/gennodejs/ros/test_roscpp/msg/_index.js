
"use strict";

let TestWithHeader = require('./TestWithHeader.js');
let TestStringInt = require('./TestStringInt.js');
let TestArray = require('./TestArray.js');
let TestEmpty = require('./TestEmpty.js');
let HeaderNotFirstMember = require('./HeaderNotFirstMember.js');
let EmbeddedExternal = require('./EmbeddedExternal.js');
let VariableLength = require('./VariableLength.js');
let CustomHeader = require('./CustomHeader.js');
let VariableLengthArrayOfExternal = require('./VariableLengthArrayOfExternal.js');
let EmbeddedVariableLength = require('./EmbeddedVariableLength.js');
let WithMemberNamedHeaderThatIsNotAHeader = require('./WithMemberNamedHeaderThatIsNotAHeader.js');
let ArrayOfFixedLength = require('./ArrayOfFixedLength.js');
let FixedLengthStringArray = require('./FixedLengthStringArray.js');
let EmbeddedFixedLength = require('./EmbeddedFixedLength.js');
let WithTime = require('./WithTime.js');
let WithDuration = require('./WithDuration.js');
let FixedLengthArrayOfExternal = require('./FixedLengthArrayOfExternal.js');
let FixedLength = require('./FixedLength.js');
let VariableLengthStringArray = require('./VariableLengthStringArray.js');
let WithHeader = require('./WithHeader.js');
let ArrayOfVariableLength = require('./ArrayOfVariableLength.js');
let Constants = require('./Constants.js');
let ThroughputMessage = require('./ThroughputMessage.js');
let LatencyMessage = require('./LatencyMessage.js');
let PointCloud = require('./PointCloud.js');
let Point32 = require('./Point32.js');
let ChannelFloat32 = require('./ChannelFloat32.js');

module.exports = {
  TestWithHeader: TestWithHeader,
  TestStringInt: TestStringInt,
  TestArray: TestArray,
  TestEmpty: TestEmpty,
  HeaderNotFirstMember: HeaderNotFirstMember,
  EmbeddedExternal: EmbeddedExternal,
  VariableLength: VariableLength,
  CustomHeader: CustomHeader,
  VariableLengthArrayOfExternal: VariableLengthArrayOfExternal,
  EmbeddedVariableLength: EmbeddedVariableLength,
  WithMemberNamedHeaderThatIsNotAHeader: WithMemberNamedHeaderThatIsNotAHeader,
  ArrayOfFixedLength: ArrayOfFixedLength,
  FixedLengthStringArray: FixedLengthStringArray,
  EmbeddedFixedLength: EmbeddedFixedLength,
  WithTime: WithTime,
  WithDuration: WithDuration,
  FixedLengthArrayOfExternal: FixedLengthArrayOfExternal,
  FixedLength: FixedLength,
  VariableLengthStringArray: VariableLengthStringArray,
  WithHeader: WithHeader,
  ArrayOfVariableLength: ArrayOfVariableLength,
  Constants: Constants,
  ThroughputMessage: ThroughputMessage,
  LatencyMessage: LatencyMessage,
  PointCloud: PointCloud,
  Point32: Point32,
  ChannelFloat32: ChannelFloat32,
};
