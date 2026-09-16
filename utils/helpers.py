"""
مجلد utils - أدوات مساعدة
Helper Functions
"""

from datetime import datetime, timedelta
import json

def format_date(date_obj):
    """تنسيق التاريخ"""
    if isinstance(date_obj, datetime):
        return date_obj.strftime('%Y-%m-%d %H:%M:%S')
    return str(date_obj)

def format_number(number):
    """تنسيق الأرقام الكبيرة"""
    if number >= 1_000_000:
        return f"{number / 1_000_000:.1f}M"
    elif number >= 1_000:
        return f"{number / 1_000:.1f}K"
    return str(number)

def calculate_engagement_rate(likes, comments, shares, views):
    """حساب معدل الانخراط"""
    if views == 0:
        return 0
    total_engagement = likes + comments + shares
    return (total_engagement / views) * 100

def validate_email(email):
    """التحقق من صحة البريد الإلكتروني"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def get_time_difference(start_time, end_time=None):
    """حساب الفرق الزمني"""
    if end_time is None:
        end_time = datetime.now()
    
    diff = end_time - start_time
    
    hours = diff.total_seconds() // 3600
    minutes = (diff.total_seconds() % 3600) // 60
    
    if hours > 0:
        return f"{int(hours)}h {int(minutes)}m"
    return f"{int(minutes)}m"

def save_to_json(data, filepath):
    """حفظ البيانات في ملف JSON"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"خطأ في حفظ الملف: {e}")
        return False

def load_from_json(filepath):
    """قراءة البيانات من ملف JSON"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"خطأ في قراءة الملف: {e}")
        return None

def generate_report(analytics_data):
    """إنشاء تقرير من بيانات التحليلات"""
    report = {
        'total_views': sum(item.get('views', 0) for item in analytics_data),
        'total_likes': sum(item.get('likes', 0) for item in analytics_data),
        'total_comments': sum(item.get('comments', 0) for item in analytics_data),
        'average_engagement': sum(item.get('engagement_rate', 0) for item in analytics_data) / len(analytics_data) if analytics_data else 0
    }
    return report
