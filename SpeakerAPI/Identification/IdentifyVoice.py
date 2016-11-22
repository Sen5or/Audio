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
    subscription_key = '136e62d920fc4696a91c1dbbf32d9a31'
    force_short_audio = 'true'

    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        subscription_key)


    profile_ids = ["99ef319e-a9a5-4a46-b679-cf2e7e4ca5f7", "de762baa-703c-4083-8595-000c3b389cb5", "3c5ef345-39ee-41bc-a5fb-63154a5b8f1e", "33ab384c-029f-4dad-8249-9a863e85e04c"]
    identification_response = helper.identify_file(
        file_path, profile_ids,
        force_short_audio.lower() == "true")
    #print('Identified Speaker = {0}'.format(identification_response.get_identified_profile_id()))
    print('Confidence = {0}'.format(identification_response.get_confidence()))        
    if (identification_response.get_identified_profile_id() == "99ef319e-a9a5-4a46-b679-cf2e7e4ca5f7"):
        print('Identified Speaker = Frank')
    elif (identification_response.get_identified_profile_id() == "de762baa-703c-4083-8595-000c3b389cb5"):
        print('Cannot Identify Speaker')
    elif (identification_response.get_identified_profile_id() == "33ab384c-029f-4dad-8249-9a863e85e04c"):
        print('Identified Speaker = YiDan')
    elif (identification_response.get_identified_profile_id() == "3c5ef345-39ee-41bc-a5fb-63154a5b8f1e"):
        print('Identified Speaker = Dhanesh')
    else:
	    print('Cannot Identify Speaker')

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