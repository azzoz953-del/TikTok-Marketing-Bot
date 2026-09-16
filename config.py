"""
ملف الإعدادات الرئيسي
Configuration File
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """الإعدادات الأساسية"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(Config):
    """إعدادات التطوير"""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///marketing_bot.db'

class ProductionConfig(Config):
    """إعدادات الإنتاج"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///marketing_bot.db')

class TestingConfig(Config):
    """إعدادات الاختبار"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# اختيار الإعدادات بناءً على البيئة
config = DevelopmentConfig
