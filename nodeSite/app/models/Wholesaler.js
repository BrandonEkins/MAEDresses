/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Wholesaler', {
    WholesalerID: {
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true,
      autoIncrement: true
    },
    Website: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    WholesalerName: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    WholesalerPhone: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    WholesalerLocation: {
      type: DataTypes.STRING(255),
      allowNull: true
    }
  }, {
    tableName: 'Wholesaler'
  });
};
