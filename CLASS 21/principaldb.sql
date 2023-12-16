
CREATE TABLE `principal` (
  `principal_id` int(11) NOT NULL,
  `principal_name` varchar(50) DEFAULT NULL,
  `experience_years` int(11) DEFAULT NULL
)

INSERT INTO `principal` (`principal_id`, `principal_name`, `experience_years`) VALUES
(1, 'Hassan', 10);


CREATE TABLE `student` (
  `student_id` int(11) NOT NULL,
  `student_name` varchar(50) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `grade` varchar(10) DEFAULT NULL,
  `principal_id` int(11) DEFAULT NULL
) 


INSERT INTO `student` (`student_id`, `student_name`, `age`, `grade`, `principal_id`) VALUES
(1, 'Tauheed', 22, 'A', 1),
(2, 'Qaseem Bhai', 28, 'A', 1),
(3, 'Ambreen Api', 30, 'A', 1);

ALTER TABLE `principal`
  ADD PRIMARY KEY (`principal_id`);

ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`),
  ADD KEY `fk_principal` (`principal_id`);


ALTER TABLE `student`
  ADD CONSTRAINT `fk_principal` FOREIGN KEY (`principal_id`) REFERENCES `principal` (`principal_id`);
COMMIT;

