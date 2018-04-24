from django.contrib.auth.models import User

class EmailAuth:
    """Authenticate a user by an email"""
    
class CaseInsensitiveAuth:
    """
    Authenticate a of User by using a case-insensitive query to check a
    combination of the supplied email/username and password.
    To avoid the risk of having two users with similar usernames,
    distinguished only by letter case (e.g. 'john' and 'John'), consider
    updating your User model to save usernames as lower case entries to
    the database.
    This will ensure all usernames have unique spellings, and as a result,
    our case insensitive query will return a single result only.
    """
    
    def authenticate(self, username=None, password=None):
        """Get and instance of user based off the email and verify the password"""
        
        
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password):
                return user
            
            return None
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        """Used by the django authentication system to retrieve a user"""
        
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
        
        