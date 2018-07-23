from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    
    # Edith has heard about a cool new online to-do app. She goes 
    # to check out its homepage
    def test_startup(self):
        self.browser.get('http://127.0.0.1:8000/')
        
        # She notices the page title and header mention to-do lists 
        self.assertIn('To-Do',self.browser.title)

        # She is invited to enter a to-do item straight away 
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to do item', 
                        'New To-Do item did not appear in table')

        # She types "Buy peacock feathers" into a text box (Edith's hobby # is tying fly-fishing lures) 
        inputbox.send_keys('Buy peacock feathers')
        
        # When she hits enter, the page updates, and now the page lists 
        inputbox.send_keys(Keys.ENTER)
    
        # "1: Buy peacock feathers" as an item in a to-do list 
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        # There is still a text box inviting her to add another item. She 

        # enters "Use peacock feathers to make a fly" (Edith is very methodical) 

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees 

        # that the site has generated a unique URL for her -- there is some 

        # explanatory text to that effect. 

        # She visits that URL - her to-do list is still there. 

        # Satisfied, she goes back to sleep
        self.fail('Finished test!') # just marker that test is finished!
if __name__ == '__main__':
    unittest.main()