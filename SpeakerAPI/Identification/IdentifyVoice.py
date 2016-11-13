import IdentificationServiceHttpClientHelper
import sys

def identify_file(file_path):
    """Identify an audio file on the server.

    Arguments:
    subscription_key -- the subscription key string
    file_path -- the audio file path for identification
    profile_ids -- an array of test profile IDs strings
    force_short_audio -- waive the recommended minimum audio limit needed for enrollment
    """
    subscription_key = "key"
    force_short_audio = 'true'

    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        subscription_key)


    profile_ids = ["id0", "id1", "id2"]
    identification_response = helper.identify_file(
        file_path, profile_ids,
        force_short_audio.lower() == "true")
    #print('Identified Speaker = {0}'.format(identification_response.get_identified_profile_id()))
    #print('Confidence = {0}'.format(identification_response.get_confidence()))        
    if (identification_response.get_identified_profile_id() == "id0"):
        print('Identified Speaker = Frank')
    elif (identification_response.get_identified_profile_id() == "id1"):
        print('Identified Speaker = YiDan')
    elif (identification_response.get_identified_profile_id() == "id2"):
        print('Identified Speaker = Dhanesh')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python IdentifyFile.py <subscription_key> <identification_file_path>'
              ' <profile_ids>...')
        print('\t<subscription_key> is the subscription key for the service')
        print('\t<identification_file_path> is the audio file path for identification')
        print('\t<force_short_audio> True/False waives the recommended minimum audio limit needed '
              'for enrollment')
        print('\t<profile_ids> the profile IDs for the profiles to identify the audio from.')
        sys.exit('Error: Incorrect Usage.')

    identify_file(sys.argv[1])