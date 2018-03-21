/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Staff', {
    StaffID: {
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true,
      autoIncrement: true
    },
    StaffName: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    Email: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    Wage: {
      type: DataTypes.INTEGER(11),
      allowNull: true
    },
    sPassword: {
      type: DataTypes.STRING(255),
      allowNull: true
    }
  }, {
    tableName: 'Staff'
  });
};
