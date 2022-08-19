-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema volunteer_job_board
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `volunteer_job_board` ;

-- -----------------------------------------------------
-- Schema volunteer_job_board
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `volunteer_job_board` DEFAULT CHARACTER SET utf8 ;
USE `volunteer_job_board` ;

-- -----------------------------------------------------
-- Table `volunteer_job_board`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `volunteer_job_board`.`users` ;

CREATE TABLE IF NOT EXISTS `volunteer_job_board`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(50) NULL,
  `phone` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `volunteer_job_board`.`jobs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `volunteer_job_board`.`jobs` ;

CREATE TABLE IF NOT EXISTS `volunteer_job_board`.`jobs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `num_volunteers` INT NULL,
  `start_time` DATETIME NULL,
  `end_time` DATETIME NULL,
  `location` VARCHAR(255) NULL,
  `description` TEXT(900) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recipes_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_recipes_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `volunteer_job_board`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `volunteer_job_board`.`signups`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `volunteer_job_board`.`signups` ;

CREATE TABLE IF NOT EXISTS `volunteer_job_board`.`signups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `job_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_comments_reviews1_idx` (`job_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `volunteer_job_board`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_comments_reviews1`
    FOREIGN KEY (`job_id`)
    REFERENCES `volunteer_job_board`.`jobs` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
