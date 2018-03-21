/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Cart', {
    CartID: {
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true,
      autoIncrement: true
    },
    NumberOfItems: {
      type: DataTypes.INTEGER(11),
      allowNull: true
    },
    TotalCost: {
      type: DataTypes.FLOAT,
      allowNull: true
    },
    ShippingCost: {
      type: DataTypes.FLOAT,
      allowNull: true
    },
    CustomerID: {
      type: DataTypes.BIGINT,
      allowNull: true,
      references: {
        model: 'Customer',
        key: 'CustomerID'
      }
    }
  }, {
    tableName: 'Cart'
  });
};
