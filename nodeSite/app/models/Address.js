/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Address', {
    AddressID: {
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true,
      autoIncrement: true
    },
    Street: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    City: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    aState: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    Zip: {
      type: DataTypes.STRING(255),
      allowNull: true
    }
  }, {
    tableName: 'Address'
  });
};
