/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Product', {
    ProductID: {
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true,
      autoIncrement: true
    },
    ShippingCost: {
      type: DataTypes.FLOAT,
      allowNull: true
    },
    ProductName: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    Color: {
      type: DataTypes.STRING(255),
      allowNull: true
    },
    Price: {
      type: DataTypes.FLOAT,
      allowNull: true
    },
    WholesalerID: {
      type: DataTypes.BIGINT,
      allowNull: true,
      references: {
        model: 'Wholesaler',
        key: 'WholesalerID'
      }
    }
  }, {
    tableName: 'Product'
  });
};
