/*
Navicat MySQL Data Transfer

Source Server         : python-mysql
Source Server Version : 50173
Source Host           : 192.168.60.130:3306
Source Database       : fort

Target Server Type    : MYSQL
Target Server Version : 50173
File Encoding         : 65001

Date: 2015-04-17 22:15:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for action_list
-- ----------------------------
DROP TABLE IF EXISTS `action_list`;
CREATE TABLE `action_list` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `user_id` int(100) DEFAULT NULL,
  `server_id` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `usersid` (`user_id`),
  KEY `serverid` (`server_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of action_list
-- ----------------------------
INSERT INTO `action_list` VALUES ('1', '1', '1');
INSERT INTO `action_list` VALUES ('2', '1', '2');
INSERT INTO `action_list` VALUES ('3', '1', '3');
INSERT INTO `action_list` VALUES ('4', '2', '2');
INSERT INTO `action_list` VALUES ('5', '2', '3');
INSERT INTO `action_list` VALUES ('6', '3', '3');

-- ----------------------------
-- Table structure for record
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record` (
  `name` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `log` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of record
-- ----------------------------
INSERT INTO `record` VALUES ('tom', '2015-04-13 01:13:40', '192.168.60.128', 'ls\n');
INSERT INTO `record` VALUES ('tom', '2015-04-13 01:13:42', '192.168.60.128', 'pwd\n');
INSERT INTO `record` VALUES ('tom', '2015-04-13 01:13:44', '192.168.60.128', 'df -h\n');
INSERT INTO `record` VALUES ('tom', '2015-04-13 01:14:00', '192.168.60.128', 'ls\n');
INSERT INTO `record` VALUES ('tom', '2015-04-13 01:14:03', '192.168.60.128', 'vi file\n');
INSERT INTO `record` VALUES ('tom', '2015-04-13 01:14:15', '192.168.60.128', 'hohello world:wq\n');
INSERT INTO `record` VALUES ('tom', '2015-04-13 01:14:16', '192.168.60.128', '\n');
INSERT INTO `record` VALUES ('tom', '2015-04-13 01:14:16', '192.168.60.128', '\n');
INSERT INTO `record` VALUES ('tom', '2015-04-13 01:14:16', '192.168.60.128', '\n');
INSERT INTO `record` VALUES ('tom', '2015-04-13 01:14:19', '192.168.60.128', 'exit\n');
INSERT INTO `record` VALUES ('jack', '2015-04-13 01:14:52', '192.168.60.129', 'ls\n');
INSERT INTO `record` VALUES ('jack', '2015-04-13 01:14:53', '192.168.60.129', 'pwd\n');
INSERT INTO `record` VALUES ('jack', '2015-04-13 01:14:55', '192.168.60.129', 'ifconfig\n');
INSERT INTO `record` VALUES ('jack', '2015-04-13 01:15:04', '192.168.60.129', 'fdiks-lis	-l\n');
INSERT INTO `record` VALUES ('jack', '2015-04-13 01:15:08', '192.168.60.129', 'exit\n');

-- ----------------------------
-- Table structure for servers
-- ----------------------------
DROP TABLE IF EXISTS `servers`;
CREATE TABLE `servers` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `server_ip` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of servers
-- ----------------------------
INSERT INTO `servers` VALUES ('1', '192.168.60.128');
INSERT INTO `servers` VALUES ('2', '192.168.60.129');
INSERT INTO `servers` VALUES ('3', '192.168.60.131');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'tom', 'tom');
INSERT INTO `users` VALUES ('2', 'jack', 'jack');
INSERT INTO `users` VALUES ('3', 'mary', 'mary');
