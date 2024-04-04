
"use strict";

let SimpleMigrated = require('./SimpleMigrated.js');
let Renamed5 = require('./Renamed5.js');
let PartiallyMigrated = require('./PartiallyMigrated.js');
let MigratedExplicit = require('./MigratedExplicit.js');
let SubUnmigrated = require('./SubUnmigrated.js');
let MigratedImplicit = require('./MigratedImplicit.js');
let MigratedMixed = require('./MigratedMixed.js');
let Unmigrated = require('./Unmigrated.js');
let Converged = require('./Converged.js');
let MigratedAddSub = require('./MigratedAddSub.js');
let Simple = require('./Simple.js');
let Constants = require('./Constants.js');

module.exports = {
  SimpleMigrated: SimpleMigrated,
  Renamed5: Renamed5,
  PartiallyMigrated: PartiallyMigrated,
  MigratedExplicit: MigratedExplicit,
  SubUnmigrated: SubUnmigrated,
  MigratedImplicit: MigratedImplicit,
  MigratedMixed: MigratedMixed,
  Unmigrated: Unmigrated,
  Converged: Converged,
  MigratedAddSub: MigratedAddSub,
  Simple: Simple,
  Constants: Constants,
};
