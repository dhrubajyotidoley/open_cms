CREATE TABLE IF NOT EXISTS `users_admin` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `user_id` varchar(50) NOT NULL DEFAULT '',
  `password` varchar(200) NOT NULL DEFAULT '',
  `email` varchar(100) NOT NULL,
  `approval` tinyint(1) NOT NULL DEFAULT '0',
  `type` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;


INSERT INTO `users_admin` (`id`, `name`, `user_id`, `password`, `email`, `approval`, `type`) VALUES
(1, 'Administrator', 'admin', '21232f297a57a5a743894a0e4a801fc3', 'info@opennirvana.com', 1, '0');
