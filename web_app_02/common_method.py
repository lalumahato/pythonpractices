class CommonMethod:
  def __init__(self):
    pass

  def created_response():
    return {
      'status': 'success',
      'message': 'New data inserted.'
    }

  def failed_response():
    return {
      'status': 'failed',
      'message': 'Something went wrong.'
    }

  def success_response(data = None):
    return {
      'status': 'success',
      'data': data 
    }