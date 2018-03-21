/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('NewOrder', {
    NewOrderID: {
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true,
      autoIncrement: true
    },
    CartID: {
      type: DataTypes.BIGINT,
      allowNull: true,
      references: {
        model: 'Cart',
        key: 'CartID'
      }
    },
    StaffID: {
      type: DataTypes.BIGINT,
      allowNull: true,
      references: {
        model: 'Staff',
        key: 'StaffID'
      }
    },
    OrderDate: {
      type: DataTypes.DATEONLY,
      allowNull: true
    }
  }, {
    tableName: 'NewOrder'
  });
};
